# WHT-markup
## Wht is happening ?
WHT is a markup language designed to make it possible for people to easily write short HTML summaries for WorldHistoryTimeline.
As you probably understand WHT compiles into HTML.

## How to use WHT
1. Simply create a file on the format <code>filname.wht</code>
2. Write your summary
3. Compile by running the script called <code>compiler.sh</code>

## Syntax
### Headers
This markup language has support for all HTML header sizes

<code>#[1-6] [text]</code>

Example: <code>#6 Hello World</code>

### Links
To add a link to your header use following syntax

<code>@[folder-name]/[...]/[file-name].html</code>

Example: <code>#6 @summaries/100.html 100</code>

### Paragraphs
Each row in the file that does not use any of the above syntax becomes a p-tag


![test](template.png)
