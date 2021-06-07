# TeddyLang #

## What is? ##

Is a very simple language to do back-end of applications did 
using [TeddyMark](https://github.com/leosavioli2019/TeddyMark) tags and HTML tags based on the syntax of python and php, but faster.

## Example ##

The example below show the numbers 0 to 9.

```html
    <main>
        <h1> Range </h1>
        <ul>
            <teddy>
                for c in range(0,10) do
                    TPRINT(f"--{c}--")
                end
            </teddy>
        </ul>
    </main>
```

Or using TeddyMark Syntax:

```markdown
    <main>
        # Range #
        %
            <teddy>
                for c in range(0,10) do
                    TPRINT(f"--{c}--")
                end
            </teddy>
        %
    </main>
```

You can see that we use to put a TeddyMark tag we use the command TPRINT, and you is correct, and to put a HTML tag you use the command PRINT. And is very simple to python but the difference is in the loops, that in the end you out do and close with end.

And the output will be this:

# Range #

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9

## How to run? ##

