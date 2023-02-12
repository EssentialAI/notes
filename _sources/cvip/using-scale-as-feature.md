# Using scale as a feature for correspondence

One important detail about the Harris corner detector is that, it does not provide the best patch size for corner detection. This means if we zoom in or zoom out of the image, harris corner detector fails.

<span class = 'high'>Harris corner detector is not scale invariant.</span>

```{note}
What is the optimal patch size to find the good features?

In other words, we would like the features to be scale invariant.
```

Harris detector is good in the sense that even though the image undergoes projective transformation, the corners are still preserved and detected by the Harris corner detector.

<!-- ```{figure} /imgs/scale-invariant.PNG

---
height: 150px
name: scale-invariant
---

Scale Invariant features for feature detection.
``` -->

```{admonition} Is there a way to modify Harris corner detector to be scale invariant?
:class: tip

The idea is to find the local maximum of the [Harris Operator](image-features.html#the-harris-operator) $f$.

For a given location, we find $f$ for $n$ different patch sizes. Finally we pick the patch size that gives the maximum value of $f$. This incorporates for the scale change issue in the Harris corner detector.
```

## A better alternative to Harris Operator $f$

**Laplacian Operator**

The Laplacian of a function $f = f(x,y)$ is defined as the divergence of its gradient which is equal to the sum of the function’s second spatial derivatives in cartesian coordinates.

```{math}
:label: laplacian

\nabla \nabla f = \nabla ^2 f= \frac{\partial ^2f}{\partial x^2} + \frac{\partial ^2 f}{\partial y^2}
```
For more information on laplacian, refer [this](https://www.plymouth.ac.uk/uploads/production/document/path/3/3744/PlymouthUniversity_MathsandStats_the_Laplacian.pdf)

For the corner detection, the Laplacian Operator becomes:

```{math}
:label: laplacian-corner
\nabla ^2 f(x,y) = I_{xx}+I_{yy}
```

There is another alternative to Laplacian detector.

```{figure} /imgs/dog.PNG

---
height: 150px
name: dog
---

Laplacian v/s Difference of Gaussians
```

Automatic patch size selection in corner detection after zoom in or zoom out.

```{figure} /imgs/auto-scale.PNG

---
height: 150px
name: auto-scale
---

Automatic patch size selection in corner detection
```

```{figure} /imgs/eigen-affine.PNG

---
height: 150px
name: eigen-affine
---

Matching under affine transformation
```

<span class = 'high'>Note that we still have not solved the correspondence problem. We have the scale invariant features, how to find what features in the left image match with the features in the right image?</span>

```{figure} /imgs/towards-scale-invariance.PNG

---
height: 150px
name: towards-scale-invariance
---

Normalization
```

```{figure} /imgs/affine-normalization-challenge.PNG

---
height: 150px
name: affine-normalization-challenge
---

Affine Normalization challenge
```

At every pixel in the image patch we calculate the vector $(I_x,I_y)$.

```{figure} /imgs/gradient-orientation.PNG

---
height: 100px
name: gradient-orientation
---

Gradient Orientation
```

```{figure} /imgs/rotational-ambiguity.PNG

---
height: 150px
name: rotational-ambiguity
---

Eliminating Rotational Ambiguity
```

```{figure} /imgs/rotational-ambiguity1.PNG

---
height: 150px
name: rotational-ambiguity1
---

Eliminating Rotational Ambiguity
```

## SIFT Vector

A more simplified version of gradient of intensity representation of ellipse is to consider a circle and calculate gradient for each pixel and maintain a histogram of gradients at every pixel.

The histogram represents the distribution of gradients in the image patch. Even when the image patch is rotated, the histogram undergoes circular shift.

```{figure} /imgs/sift-features.PNG

---
height: 150px
name: sift-features
---

SIFT Features
```

```{figure} /imgs/sift-hand-drawn.PNG

---
height: 150px
name: sift-hand-drawn
---

SIFT Features
```

<span class = 'high'>An important detail to note is that SIFT features consider the gradient of intensity values and not the pixel values.</span>









