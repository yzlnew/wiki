---
type: source-summary
status: active
tags: [freshrss, rss, inbox]
source_count: 1
updated: 2026-04-08
source_url: https://old.reddit.com/r/LocalLLaMA/comments/1sfj075/gemma_4_llamacpp_tool_calls_and_tool_results/
feed_source: LocalLlama
published: 2026-04-08T12:35:57+08:00
decision: maybe
score: 64
generator: scripts/update_freshrss.py
---

# Gemma 4, llama.cpp, tool calls, and tool results - ChatGPT fixed it for me

## Summary

- source_feed: `LocalLlama`
- original_url: https://old.reddit.com/r/LocalLLaMA/comments/1sfj075/gemma_4_llamacpp_tool_calls_and_tool_results/
- published: `2026-04-08T12:35:57+08:00`
- filter_reason: Relevant to agent-workflows but signal is mixed before full-text fetch.

## Feed Metadata

- source_home: https://old.reddit.com/r/LocalLlama/
- categories: `user/-/state/com.google/reading-list`, `user/-/label/未分类`, `user/-/state/org.freshrss/main`, `r/LocalLLaMA`
- feed_summary: I have been trying to use Gemma 4 for tool calling but kept getting errors like a lot of people. I asked ChatGPT to help me figure it out. Gave it the chat template, it had me try a few different messages, and the tool calls kept breaking. It could make a tool call but would not take the result (either crash with a...
- fetched_page_title: Gemma 4, llama.cpp, tool calls, and tool results - ChatGPT fixed it for me : LocalLLaMA
- fetched_page_description: I have been trying to use Gemma 4 for tool calling but kept getting errors like a lot of people. I asked ChatGPT to help me figure it out. Gave...

## Full Text

I have been trying to use Gemma 4 for tool calling but kept getting errors like a lot of people.
I asked ChatGPT to help me figure it out. Gave it the chat template, it had me try a few different messages, and the tool calls kept breaking. It could make a tool call but would not take the result (either crash with a 400/500 error or just make another tool call again). ChatGPT suggested I look at the llama.cpp code to figure it out - gave me a few things to search for which I found in common/chat.cpp.
I had it review the code and come up with a fix. Based on the troubleshooting we already did, it was able to figure out some things to try. First few didn't fix it so we added a bunch of logging. Eventually, we got it working though!
This is what ChatGPT had to say about the issues:
Gemma 4’s template/tool flow is different from the usual OpenAI-ish flow. The raw OpenAI-style assistant/tool history needs to be converted into Gemma-style tool_responses at the right point in the pipeline.
In common_chat_templates_apply_jinja(), the Gemma tool-response conversion needed to happen earlier, before the generic prompt diff / generation-prompt derivation path.
In common_chat_try_specialized_template(), that same Gemma conversion should not run a second time.
In workaround::gemma4_model_turn_builder::build(), the synthesized assistant message needed explicit empty content.
Biggest actual crash bug: In workaround::gemma4_model_turn_builder::collect_result(), it was trying to parse arbitrary string tool output as JSON. That blows up on normal tool results like: [DIR] Components etc. Once I stopped auto-parsing arbitrary string tool output as JSON and just kept string results as strings, the Gemma continuation path started working.
build() - it added that part based on what it saw in the chat template (needs empty content instead of no content).
My test prompt was a continuation after tool call results were added (User->Assistant w/tool call->Tool result). The tool result happened to start with "[" (directory listing - "[DIR] Components") which tripped up some json parsing code. That is what it's talking about in collect_result() above.
I tested it a bit in my own program and it works! I tested Qwen3.5 and it still works too so it didn't break anything too badly.
It's 100% ChatGPT generated code. Llama.cpp probably doesn't want AI slop code (I hope so anyways) but I still wanted to share it. Maybe it will inspire someone to do whatever is needed to update llama.cpp.
Here is the gemma4_fix.diff I created (from ChatGPT's code). I hope it helps somebody. Should I have posted the updated methods instead of a diff? BTW - this is my first ever Reddit post.
diff --git a/common/chat.cpp b/common/chat.cpp index 5b93c5887..7fb3ea2de 100644 --- a/common/chat.cpp +++ b/common/chat.cpp @@ -1729,59 +1729,60 @@ struct gemma4_model_turn_builder { } } - void collect_result(const json & curr) { - json response; - if (curr.contains("content")) { - const auto & content = curr.at("content"); - if (content.is_string()) { - // Try to parse the content as JSON; fall back to raw string - try { - response = json::parse(content.get<std::string>()); - } catch (...) { - response = content; - } - } else { - response = content; - } - } - - std::string name; - - // Match name with corresponding tool call - size_t idx = tool_responses.size(); - if (idx < tool_calls.size()) { - auto & tc = tool_calls[idx]; - if (tc.contains("function")) { - name = tc.at("function").value("name", ""); - } - } - - // Fallback to the tool call id - if (name.empty()) { - name = curr.value("tool_call_id", ""); - } - - tool_responses.push_back({{"name", name}, {"response", response}}); - } - - json build() { - collect(); - - json msg = { - {"role", "assistant"}, - {"tool_calls", tool_calls}, - }; - if (!tool_responses.empty()) { - msg["tool_responses"] = tool_responses; - } - if (!content.is_null()) { - msg["content"] = content; - } - if (!reasoning_content.is_null()) { - msg["reasoning_content"] = reasoning_content; - } - return msg; - } +void collect_result(const json & curr) { +json response; +if (curr.contains("content")) { +const auto & content = curr.at("content"); +if (content.is_string()) { +// Keep raw string tool output as-is. Arbitrary tool text is not +// necessarily valid JSON. +response = content.get<std::string>(); +} else { +response = content; +} +} + +std::string name; + +// Match name with corresponding tool call +size_t idx = tool_responses.size(); +if (idx < tool_calls.size()) { +auto & tc = tool_calls[idx]; +if (tc.contains("function")) { +const auto & fn = tc.at("function"); +if (fn.contains("name") && fn.at("name").is_string()) { +name = fn.at("name").get<std::string>(); +} +} +} + +// Fallback to the tool call id +if (name.empty()) { +name = curr.value("tool_call_id", ""); +} + +tool_responses.push_back({{"name", name}, {"response", response}}); +} + +json build() { +collect(); + +json msg = { +{"role", "assistant"}, +{"tool_calls", tool_calls}, +{"content", ""}, +}; +if (!tool_responses.empty()) { +msg["tool_responses"] = tool_responses; +} +if (!content.is_null()) { +msg["content"] = content; +} +if (!reasoning_content.is_null()) { +msg["reasoning_content"] = reasoning_content; +} +return msg; +} static bool has_content(const json & msg) { if (!msg.contains("content") || msg.at("content").is_null()) { @@ -1914,7 +1915,6 @@ std::optional<common_chat_params> common_chat_try_specialized_template( // Gemma4 format detection if (src.find("'<|tool_call>call:'") != std::string::npos) { - workaround::convert_tool_responses_gemma4(params.messages); return common_chat_params_init_gemma4(tmpl, params); } @@ -1958,14 +1958,10 @@ static common_chat_params common_chat_templates_apply_jinja(const struct common_ workaround::func_args_not_string(params.messages); } - params.add_generation_prompt = false; - std::string no_gen_prompt = common_chat_template_direct_apply_impl(tmpl, params); - params.add_generation_prompt = true; - std::string gen_prompt = common_chat_template_direct_apply_impl(tmpl, params); - auto diff = calculate_diff_split(no_gen_prompt, gen_prompt); - params.generation_prompt = diff.right; - - params.add_generation_prompt = inputs.add_generation_prompt; + const bool is_gemma4 = src.find("'<|tool_call>call:'") != std::string::npos; + if (is_gemma4) { + workaround::convert_tool_responses_gemma4(params.messages); + } params.extra_context = common_chat_extra_context(); for (auto el : inputs.chat_template_kwargs) { @@ -2005,6 +2001,24 @@ static common_chat_params common_chat_templates_apply_jinja(const struct common_ return data; } + if (is_gemma4) { + params.add_generation_prompt = inputs.add_generation_prompt; + params.generation_prompt = "<|channel>thought\n<channel|>"; + + auto result = common_chat_params_init_gemma4(tmpl, params); + result.generation_prompt = params.generation_prompt; + return result; + } + + params.add_generation_prompt = false; + std::string no_gen_prompt = common_chat_template_direct_apply_impl(tmpl, params); + params.add_generation_prompt = true; + std::string gen_prompt = common_chat_template_direct_apply_impl(tmpl, params); + auto diff = calculate_diff_split(no_gen_prompt, gen_prompt); + params.generation_prompt = diff.right; + + params.add_generation_prompt = inputs.add_generation_prompt; + if (auto result = common_chat_try_specialized_template(tmpl, src, params)) { result->generation_prompt = params.generation_prompt; return *result; @@ -2187,4 +2201,3 @@ std::map<std::string, bool> common_chat_templates_get_caps(const common_chat_tem GGML_ASSERT(chat_templates->template_default != nullptr); return chat_templates->template_default->caps.to_map(); } -
submitted by /u/TheProgrammer-231
[link] [comments]
