---
title: "03 — How Computers Run Programs"
published: false
---

**Wednesday, September 2 · Zoom**

**Reading:** *Python for Everybody*, §1.2, §1.6, §1.9, §1.11, §2.13

**Goal for today:** to understand what was actually happening inside the machine on Monday.

I am travelling today, so we meet on Zoom. **You do not need to code along** — close IDLE, no machine required. This is the one day this unit that is about ideas rather than typing, and all of it is on Test 1.

You just spent a full period on Monday making a computer do something. Today we look at what it was doing while you did.

---

## 1. What is actually in there

Chapter 1 walks through the hardware. Four parts matter to us.

**Central Processing Unit (CPU).** Does the actual work, one instruction at a time, very fast — billions per second. It is astonishingly stupid and astonishingly quick, which is exactly the combination that makes precision matter.

**Main Memory (RAM).** The CPU's workspace. Fast, and **erased when the power goes off**. Every variable in your running program lives here.

**Secondary Memory (disk).** Slow, and it survives a power cycle. Your `.py` files live here.

**Input and Output Devices.** Keyboard, screen, mouse, network.

### The one consequence worth remembering

**The values in your running program are in main memory, and they disappear when the program ends.**

On Monday, `hello.py` asked for your name, held it, printed a greeting, and then forgot it completely. Run it again and it has no memory that you ever existed. That is not a limitation you worked around — that is simply what a running program is.

This is why we save files. It is also why an entire unit later in the semester is about reading and writing files: at some point you will want a program to remember something after it stops, and putting it on disk is the only way to do that.

<details class="code-example" markdown="1">
<summary>Worth a moment — where does the typing go?</summary>

When you ran Monday's `pay.py` and typed `35`, that number travelled: keyboard (input device) → main memory, where `input` put it and gave it the name `hours` → CPU, which did the multiplication → main memory again, holding `pay` → screen (output device), via `print`.

At no point did it touch the disk. Close the window and every bit of it is gone.

</details>

---

## 2. Interpreter and compiler

Python is a **high-level language**. So are Java, C, and JavaScript. They are written to be readable by people. The CPU cannot read any of them — it only understands **machine language**, which is numbers.

Something has to translate. There are two ways to do it, and the difference has a name you need to know.

**A compiler** translates the whole program in advance, producing a machine-language file. You run that file afterward. Translation happens once; running happens whenever you like.

**An interpreter** reads your program a line at a time, translating and executing as it goes. There is no separate translated file — the interpreter is doing the work every time the program runs.

**Python is interpreted.** That is why the `>>>` prompt exists at all: an interpreter is already reading and executing one line at a time, so there is nothing strange about it reading a line you just typed. A compiled language cannot really offer that, which is why C has no equivalent of the Python prompt.

When you press **F5** in IDLE, you are handing your file to the Python interpreter and asking it to work through it top to bottom.

<details class="code-example" markdown="1">
<summary>Why this explains something you already noticed</summary>

Remember from Lecture 1 that a syntax error stops your program before *anything* runs, even if the error is on the last line — but a runtime error lets the earlier lines run first, and only then crashes.

That is the interpreter at work. It reads the whole file to check that it is well-formed Python before executing any of it; that check is where syntax errors come from. Then it goes back to the top and starts executing, and errors found during *that* pass are runtime errors.

Same file, two passes, two different kinds of failure.

</details>

---

## 3. The building blocks of programs

Here is the part that is really a map of the rest of the semester. Section 1.9 claims that every program ever written is built from six things.

**Input.** Get data from the outside world — keyboard, file, network. *You have done this: `input`.*

**Output.** Put results out — screen, file. *You have done this: `print`.*

**Sequential execution.** Perform statements one after another, in order. *You have done this. Every program you have written so far is nothing but this.*

**Conditional execution.** Check a condition and run — or skip — some statements accordingly. *Chapter 3, right after Test 1.* This is how a program handles the user typing something that is not a number instead of just crashing, which is the loose end we left on August 28.

**Repeated execution.** Do something over and over, usually with variation. *Chapter 5.* This is how you handle a thousand inputs without writing a thousand lines.

**Reuse.** Write a set of instructions once, name it, and use it wherever you need it. *Chapter 4.* You have been *using* reuse all along — `print`, `input`, `int`, `float`, and `type` are all somebody else's named instructions. Soon you will write your own.

That is the whole course. Three of the six are behind you already, which is worth knowing on a day when programming feels large and unbounded. It is not unbounded. It is six things.

---

## 4. Three kinds of wrong, revisited

We met these in Lecture 1 as a table. You have since made all three for real, so they should land differently now.

| Kind | When it bites | How you find out |
|---|---|---|
| **Syntax error** | Before anything runs | Python refuses to start and points at a line |
| **Runtime error** | Partway through | It crashes, with a `Traceback` |
| **Semantic error** | Never | It finishes, cheerfully, with the wrong answer |

**Syntax errors** are typos: an unclosed quote, an unclosed parenthesis, a keyword used as a variable name. They are annoying and they are never deep. The message points at the line, or occasionally the line *after* the real problem.

**Runtime errors** mean the instruction was well-formed but impossible to carry out. `int('hello')` is a perfectly legal sentence about an impossible request. Monday's `TypeError` from multiplying two strings was one of these.

**Semantic errors** are the dangerous ones, and they are the reason this course grades against sample output. Your program ran. It printed something. It printed the wrong thing, and it was completely confident. Nothing in the machine will ever tell you — the machine did what you said.

<details class="code-example" markdown="1">
<summary>Predict the kind — we will do these live</summary>

For each one: syntax, runtime, or semantic?

1. `print('Total:' total)`
2. `pay = hours * rate` where `hours` came straight from `input` with no conversion
3. `average = a + b / 2`
4. `print("Hello)`
5. `celsius = int(input('Temperature: '))` and the user types `98.6`

Answers: 1 syntax (missing comma). 2 runtime (`TypeError`, it crashes). 3 semantic — it runs, and computes `a + (b/2)`, which is not the average. 4 syntax. 5 runtime (`ValueError` — `int` cannot take `'98.6'`).

Number 3 is the one to be frightened of.

</details>

---

## 5. Debugging as a practice

Debugging is not something you do when you are unlucky. It is most of programming, for everyone, permanently. The difference between people who find bugs quickly and people who do not is method, not talent.

Four habits, all of which you can start using this week:

**Read the last line of the error first.** Not the whole traceback. The last line names the error type and describes the problem. Everything above it is the route Python took to get there, which matters later in the semester and almost never now.

**Grow programs a few lines at a time.** If you write four lines, run them, and they work, then write four more and something breaks — you know which four lines did it. If you write twenty and run them once, you have twenty suspects. This is why we build the in-class examples in stages.

**When you are confused, ask Python.** The `>>>` prompt is right there. `type(hours)` answers "is this a number or is it text?" in four seconds. Guessing takes longer and is often wrong.

**Test against an answer you already know.** Run the program on numbers you can do in your head. This is the *only* defense against semantic errors, and it is why every assignment in this course hands you a table of expected output.

And one more, which is not in the book: **when you are properly stuck, describe the problem out loud to somebody.** You will frequently solve it halfway through the sentence. This works on classmates, on me in office hours, and — genuinely — on an inanimate object.

---

## What Test 1 will ask from today

Test 1 is Friday, September 11, and it covers Chapters 1 and 2. From this material, be ready to:

- [ ] Name the four parts of the machine and say what each does.
- [ ] Explain why the values in a running program disappear when it ends, and what you do about it.
- [ ] Define **interpreter** and **compiler** and say which one Python uses.
- [ ] List the six building blocks of programs, and say which ones you have used so far.
- [ ] Given a broken program, say whether the mistake is syntax, runtime, or semantic — and explain why the semantic one is the worst.
- [ ] Describe how you would go about finding a bug in a program that runs but prints the wrong number.

## Before Friday

1. **Read §1.2, §1.6, §1.9, §1.11, and §2.13.** Short sections, and you now have the context to make them mean something.
2. **Look back at Monday's assignment.** Find one thing that went wrong for you — anything, including a typo — and be ready to say which of the three kinds it was.
3. Nothing to submit.

Friday we are back in the room and back on the keyboards, and we pick up the operators I have been deferring since the first day: what to do with a remainder, how to raise something to a power, and what `+` really does to two pieces of text. That is everything you need for the second programming assignment.
