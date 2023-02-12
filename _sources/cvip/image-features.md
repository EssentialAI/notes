# Image Features and Matching

Finding [fundamental matrix](image-rectification.html#the-fundamental-matrix) is kind of a chicken-and-egg problem. To map the coordinates between left and right cameras, we require the fundamental matrix, but to find the fundamental matrix, we want at least 8 corresponding image coordinates between left and right image planes.


We use image features to solve this correspondence problem. Applications of these image-features based mapping can be found in Panorama creation.

Local features in the image are used to find these corresponding points of objects.

**Advantages of local features.**

* Locality - robust to occlusion and clutter.
* Distinctiveness - can differentiate a large database of objects.
* Quantify - hundreds or thousands in a single image.
* Efficiency - real-time performance achievable.
* Generality - exploit different types of features in different situations.

**Challenges**
* Repeatability
* Uniqueness
* Invariance

Local features are usually a patch of $n \times n$ dimensions.

```{note} 
This leads us to a question. "Which are the best local features to solve the correspondence problem?"
```
```{figure} /imgs/which-features.PNG

---
height: 150px
name: which features
---

Feature selection for correspondence
```

Intuitively, <span class = 'high'>corners are the good features</span>, because corners are easier to identify (solving the uniqueness challenge) with low ambiguity.

```{figure} /imgs/corners-as-features.PNG

---
height: 150px
name: corners as features
---

Corners as features
```

**Harris corner detector gives a mathematical approach for determining the performance of an image patch w.r.t. movement of the patch along x and y axes.**

## The math behind Harris corner detector

Each value at every pixel represents its intensity from $0 \rightarrow 255$. When the image patch is translated across $x$ and $y$ axis, the measure of intensity at each pixel changes. If this change is drastic, then the location could be a corner. This would be a good candidate for correspondence matching.

The difference in the intensity between pixel locations of two patches is simply a <span class = 'high'>square of difference of the intensity values at every pixel for first and second patch.</span>

```{math}
:label: delta-I
\Delta I = \sum_{i,j}({I_{i,j}}_{\text{patch-1}}-{I_{i,j}}_{\text{patch-2}})^2
```

If $\Delta I$ is low, it shows that the feature is bad. The change in Intensity $\Delta I$ depends on the movement along $x$ and $y$ axes. This movement along an axis helps us determine the geometry of the patch.

To acheive the above patch movement along $x$ and $y$ axes, we generalize `eq`{delta-I} as:

```{figure} /imgs/delta-I.PNG

---
height: 150px
name: delta-I
---

Change in the intensity of pixels with movement of image patch.
```

Using the taylor series expansion, we represent: 

$$
I(x+u, y+v) = I(x,y)+ u{I'}_x(x,y) + v{I'}_y(x,y)
$$

The matrix form of $E(u,v)$ can be written as:

```{math}
:label: harris-corner
E(u,v) \approx \begin{bmatrix}
u & v
\end{bmatrix} \sum_{x,y}w(x,y)
\begin{bmatrix}
I_x^2 & I_xI_y \\
I_x I_y & I_y^2
\end{bmatrix} \begin{bmatrix} u \\
v \end{bmatrix}
```

$I_x$ and $I_y$ are the gradients of Intensity function along $x$ and $y$ axes.

```{figure} /imgs/E_u_v.PNG

---
height: 150px
name: Harris
---

Harris corner detector equation.
```

$w(x,y)$ demonstrates the importance of difference in intensity of pixels at a location. Sometimes, the pixels at the center can be more important than edge pixels.

<span class = 'high'>A good features has $E(u,v)$ as a very high value.</span>

```{admonition} $I_x$ and $I_y$ elaborated
:class: tip

$I_x$ and $I_y$ are the partial derivatives of the function $I$ w.r.t. $x$ and $y$ respectively.

$$
I_x = \frac{\partial I(x,y)}{\partial x}
$$

$$
I_y = \frac{\partial I(x,y)}{\partial y}
$$

<span class = 'high'>Along the vertical edge $I_y = 0$, $I_x = \text{large}$</span>

<span class = 'high'>Along the horizontal edge $I_x = 0$, $I_y = \text{large}$.</span>

<span class = 'high'>At a corner $I_x = \text{large}, I_y = \text{large}$.</span>
```

Using geometry and the concept of eigen values, the matrix $M$ is represented in the form of eigen values, $\lambda _1$ and $\lambda _2$

Eigen values represent the maximum change in $x$ and $y$ direction of $I$.

```{figure} /imgs/l1-l2.PNG

---
height: 150px
name: l1-l2
---

Eigen value representation of gradients $I_x$ and $I_y$
```


```{figure} /imgs/class-by-eigen.PNG

---
height: 150px
name: class-by-eigen
---

Classification of image patches using eigen values.
```

```{figure} /imgs/l1-l2-1.PNG

---
height: 150px
name: l1-l2-1
---

Eigen value representation of $M$
```

```{figure} /imgs/l1-l2-2.PNG

---
height: 150px
class: caption
name: l1_l2_2
---

The Matrix $H$.
```

```{figure} /imgs/l1-l2-3.PNG

---
height: 150px
name: l1-l2-3
---

Eigen values of $H$
```

```{figure} /imgs/l1-l2-4.PNG

---
height: 150px
name: l1-l2-4
---

Detection on a chess board
```
```{note}
At every pixel we calculate the matrix $M$.

$\lambda_+$ is the amount of increase in the direction of largest increase. <span class = 'high'>It is responsible for the detection of corners as well as the edges.</span>

$\lambda_-$ is the amount of increase in the direction of smallest increase. <span class = 'high'>It is responsible for the detection of corners in the image.</span>
```

```{figure} /imgs/l1-l2-5.PNG

---
height: 150px
name: l1-l2-5
---

Detection on a chess board
```

## The Harris Operator

```{figure} /imgs/harris-operator.PNG

---
height: 150px
name: harris-operator
---

Harris Operator for the matrix $H$ in `Fig-33`
```

The Harris Operator $f$ is smoother than $\lambda_-$. $\lambda_-$ is more picky.

```{figure} /imgs/harris-operator1.PNG

---
height: 150px
name: harris-operator1
---

Harris Operator v/s $\lambda_-$
```

Input             |  Detection | Output 
:-------------------------:|:-------------------------:|:-------------------------:
![](/imgs/harris-example-left.PNG)  |  ![](/imgs/harris-example-right.PNG)  | ![](/imgs/harris-example-bw.PNG)

Even though the image, is tilted (or projected), the harris corner detector is able to find the corners in the image.

```{note}
Using harris corner detector, it might seem that we can find the corresponding points to find the fundamental matrix. However, these points are just the candidates for the best points to consider for correspondence. We have to remove outliers from these corners, along with other important challenges that arise from Harris Corner detector.

<span class= 'high'>Another important point is that, while Harris corner detector gives you all the corners in the image, it does not give you the correspondence between the corners.</span>
```


















