# BracketSpacer

As seeked by [/u/HighR0ller](https://www.reddit.com/r/SublimeText/comments/64car3/automatically_add_space_in_braces/).

## Adds space on the matching bracket (on the same line)

Press spacebar twice to add spaces. Binding to a single spacebar press is unfortunately not possible with sublime.

With `|` being the cursor:

```
[|foo]
<space><space>
[ |foo ]
```

```
{|{ foo: bar }}
<space><space>
{ |{ foo: bar } }
```

```
(|)
<space><space>
( | )
```

## Removes space on the matching bracket (on the same line)

Press backspace after a space char inside of brackets.

```
[ |foo ]
<backspace>
[|foo]
```

```
{ |{ foo: bar } }
<backspace>
{|{ foo: bar }}
```

```
( | )
<backspace>
(|)
```
