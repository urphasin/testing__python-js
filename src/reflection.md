ask me 3 things to see if i understand my code

Nice. I looked at your file 

learn_turtle

 — it contains:

from turtle import *

forward(200)
left(120)
forward(200)

Now I’m going to test your understanding 👇

1️⃣ Geometry Question

After the first forward(200) and left(120), what angle is the turtle facing relative to where it started?

Is it:

A) 60°

B) 120°

C) 180°

D) 240°

Explain why.

2️⃣ Shape Question

If you add:

left(120)
forward(200)

What complete shape would the turtle draw?

And why does that specific angle matter?

3️⃣ Concept Question

What direction is the turtle facing before any commands run?

Up?

Down?

Left?

Right?

And how do you know?

Answer those, and I’ll know exactly how well you understand what your code is doing.

Sources
120

Good — ✅ 120° is correct.

Now I want you to go deeper.

Why is it 120°?

The turtle:

Starts facing right (0°)

Moves forward 200 (no direction change)

Turns left 120°

So now it is facing 120° counterclockwise from the positive x-axis.

Now answer the next two:

2️⃣ If we add:
left(120)
forward(200)

What full shape is created?

And why does 120° specifically matter?

3️⃣ What direction does the turtle face before any code runs?

Be precise. Not just “right” — think in degrees.

Let’s see how sharp you are.

maybe create triangle

🔥 YES. Good instinct.

It does create a triangle.

Now let’s sharpen your understanding.

Why is it a triangle?

You move:

Forward 200

Left 120°

Forward 200

Left 120°

Forward 200

That means:

3 equal sides (all 200)

3 equal turns (120° each)

That creates an equilateral triangle.

Why 120° specifically?

Because:

For a regular polygon:

Exterior angle
=
360
°
𝑛
Exterior angle=
n
360°
	​


For a triangle:

360
°
3
=
120
°
3
360°
	​

=120°

So turning 120° three times closes the shape perfectly.

If you turned:

90° → square (4 sides)

60° → hexagon (6 sides)

72° → pentagon (5 sides)

You’re starting to think geometrically now 👌

Now answer this last one carefully:

Before any commands run, what direction is the turtle facing in degrees?

Not just “right.”
Give me the exact angle.

it faces right0

💯 YES.

The turtle starts facing 0°, which is:

Along the positive x-axis

To the right

In turtle graphics:

0° → Right

90° → Up

180° → Left

270° → Down

So your understanding is solid so far.

Now I want to stretch your brain a little.

If you changed your code to:

from turtle import *

forward(200)
left(60)
forward(200)

Would that still help form an equilateral triangle?

Or would something different happen?

Think carefully before answering.