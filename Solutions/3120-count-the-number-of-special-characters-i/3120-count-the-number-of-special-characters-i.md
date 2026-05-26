<h1>3120 - Count the Number of Special Characters I</h1>
<h2>Difficulty: Easy - <a href="https://leetcode.com/problems/count-the-number-of-special-characters-i/">count-the-number-of-special-characters-i</a></h2>

<p>A character is called <strong>special</strong> if it appears <strong>both</strong> in lowercase and uppercase in the string.</p>

<p>Return the number of special characters in <code>word</code>.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong>
<span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">word = "aaAbcBC"</span></p>

<p><strong>Output:</strong>
<span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">3</span></p>

<p><strong>Explanation:</strong> The special characters are <code>'a'</code>, <code>'b'</code>, and <code>'c'</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong>
<span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">word = "abc"</span></p>

<p><strong>Output:</strong>
<span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">0</span></p>

<p><strong>Explanation:</strong> No character appears in both lowercase and uppercase.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong>
<span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">word = "abBCab"</span></p>

<p><strong>Output:</strong>
<span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">1</span></p>

<p><strong>Explanation:</strong> The only special character is <code>'b'</code>.</p>
</div>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= word.length &lt;= 50</code></li>
    <li><code>word</code> consists of only lowercase and uppercase English letters.</li>
</ul>