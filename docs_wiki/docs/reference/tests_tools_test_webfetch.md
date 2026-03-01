---
title: "tests.tools.test_webfetch"
tldr: "Module tests.tools.test_webfetch"
tags: [reference, api]
---

# `tests.tools.test_webfetch`

**Source:** [`tests/tools/test_webfetch.py`](tests/tools/test_webfetch.py) · 253 lines

## `webfetch()`

```python
def webfetch()
```

**Source:** [`tests/tools/test_webfetch.py#L13`](tests/tools/test_webfetch.py#L13)

## `webfetch_small()`

```python
def webfetch_small()
```

**Source:** [`tests/tools/test_webfetch.py#L19`](tests/tools/test_webfetch.py#L19)

## `test_bare_domain_gets_https()`

```python
async def test_bare_domain_gets_https(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L26`](tests/tools/test_webfetch.py#L26)

## `test_http_url_stays_http()`

```python
async def test_http_url_stays_http(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L39`](tests/tools/test_webfetch.py#L39)

## `test_https_url_stays_https()`

```python
async def test_https_url_stays_https(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L51`](tests/tools/test_webfetch.py#L51)

## `test_protocol_relative_url_normalized()`

```python
async def test_protocol_relative_url_normalized(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L63`](tests/tools/test_webfetch.py#L63)

## `test_ftp_scheme_rejected()`

```python
async def test_ftp_scheme_rejected(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L75`](tests/tools/test_webfetch.py#L75)

## `test_empty_url_rejected()`

```python
async def test_empty_url_rejected(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L81`](tests/tools/test_webfetch.py#L81)

## `test_html_converted_to_markdown()`

```python
async def test_html_converted_to_markdown(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L88`](tests/tools/test_webfetch.py#L88)

## `test_plain_text_unchanged()`

```python
async def test_plain_text_unchanged(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L102`](tests/tools/test_webfetch.py#L102)

## `test_scripts_stripped_from_markdown()`

```python
async def test_scripts_stripped_from_markdown(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L116`](tests/tools/test_webfetch.py#L116)

## `test_cloudflare_retry_on_challenge()`

```python
async def test_cloudflare_retry_on_challenge(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L131`](tests/tools/test_webfetch.py#L131)

## `test_regular_403_not_retried()`

```python
async def test_regular_403_not_retried(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L147`](tests/tools/test_webfetch.py#L147)

## `test_truncates_to_max_bytes_with_disclaimer()`

```python
async def test_truncates_to_max_bytes_with_disclaimer(webfetch_small)
```

**Source:** [`tests/tools/test_webfetch.py#L158`](tests/tools/test_webfetch.py#L158)

## `test_truncates_html_with_disclaimer()`

```python
async def test_truncates_html_with_disclaimer(webfetch_small)
```

**Source:** [`tests/tools/test_webfetch.py#L174`](tests/tools/test_webfetch.py#L174)

## `test_http_404_raises_tool_error()`

```python
async def test_http_404_raises_tool_error(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L196`](tests/tools/test_webfetch.py#L196)

## `test_http_500_raises_tool_error()`

```python
async def test_http_500_raises_tool_error(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L204`](tests/tools/test_webfetch.py#L204)

## `test_timeout_raises_tool_error()`

```python
async def test_timeout_raises_tool_error(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L212`](tests/tools/test_webfetch.py#L212)

## `test_network_error_raises_tool_error()`

```python
async def test_network_error_raises_tool_error(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L220`](tests/tools/test_webfetch.py#L220)

## `test_negative_timeout_rejected()`

```python
async def test_negative_timeout_rejected(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L229`](tests/tools/test_webfetch.py#L229)

## `test_zero_timeout_rejected()`

```python
async def test_zero_timeout_rejected(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L237`](tests/tools/test_webfetch.py#L237)

## `test_over_max_timeout_rejected()`

```python
async def test_over_max_timeout_rejected(webfetch)
```

**Source:** [`tests/tools/test_webfetch.py#L245`](tests/tools/test_webfetch.py#L245)

## `test_get_status_text()`

```python
def test_get_status_text()
```

**Source:** [`tests/tools/test_webfetch.py#L252`](tests/tools/test_webfetch.py#L252)

