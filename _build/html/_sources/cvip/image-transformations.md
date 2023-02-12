# Image Transformations

Let us recall from the previous chapter that camera is a mapping from a 3D point $[X_w, Y_w, Z_w]^T$ to a 2D point $[u,v]$ on an image plane. (pixel location).

This chapter of the course deals about the 2D $\rightarrow$ 2D transformations.

Image filtering and Image warping are some examples of the 2D to 2D transformations. Image filtering does not change the size or shape of the object, it just changes the colors or the texture of objects. Image warping reconfigures the pixel location and hence can change the size/shape of the object in the image.

Image filtering changes the **range** of the image, whereas image warping changes the **domain** of the image. Projector is a good example of image warping.

Examples of parametric warps:
1. Translation
2. Rotation
3. Aspect (change the dimensions of the image display)
4. Affine (parallel lines are still parallel)
5. Perspective (parallel lines are not parallel)
6. Cylindrical

<span class = 'high'>3D to 2D we have 11 independent parameters (intrinsic and extrinsic). 2D to 2D mapping has 4 parameters.</span>

```{math}
:label: 2d_map
\begin{bmatrix}
x' \\
y'\end{bmatrix} = M_{2 \times 2} \begin{bmatrix}
x \\
y\end{bmatrix}
```

## Scaling
Scaling happens after we shoot the image.

It is defined by multiplying each component in the image by a scalar. Uniform scaling means this scalar is the same for all components.

```{figure} /imgs/scaling.PNG

---
height: 150px
name: scaling
---

2D scaling
```

One important thing to note here is that scaling not only increases the size of the object (house in this case), but also changes the distance between the pixel and the origin. Depending on the values of the scaling factors along $x$ and $y$, the image may either shrink in size of expand.

Scaling operation:

$$ x' = ax $$
$$ y' = by $$
 
$$
\begin{bmatrix}
x' \\
y'\end{bmatrix} = \begin{bmatrix}a & 0 \\
0 & b\end{bmatrix} \begin{bmatrix}
x \\
y\end{bmatrix}
$$

## 2D Rotation

Rotate a point $(x,y)$ <span class = 'high'>counter clockwise</span>, by an angle $\theta$.

```{figure} /imgs/2d_rotation.PNG

---
height: 150px
name: 2d_rotation
---

2D rotation
```
$$
\begin{bmatrix}
x' \\
y'\end{bmatrix} = \begin{bmatrix}cos(\theta) & -sin(\theta) \\
sin(\theta) & cos(\theta)\end{bmatrix} \begin{bmatrix}
x \\
y\end{bmatrix}
$$

Even though $sin(\theta)$ and $cos(\theta)$ are non-linear functions of $\theta$, $x'$ and $y'$ are linear combinations of $x$ and $y$ . For more information about 3D rotation, refer [here](https://cs-courses.mines.edu/csci507/schedule/06/3Dto3DTransforms.pdf)

## 2D Translation

Using $2 \times 2$ matrix, we cannot perform translation.

$$ x' = x+t_x $$
$$y' = y+t_y$$

To perform translation using matrix multiplication, we perform homegeneousation. Translation matrix will become:

$$
T = \begin{bmatrix} 1& 0 & t_x\\
0 & 1 & t_y \\
0 & 0& 1\end{bmatrix}
$$

$2 \times 2$ matrix $M$ cannot perform translation. Hence, we increase the dimensions to $3 \times 3$.

```{figure} /imgs/homogeneous.PNG

---
height: 150px
name: homogeneous
---

2D Transformations
```

```{math}
:label: trans

\begin{bmatrix}x'\\
y' \\
w'\end{bmatrix} = \begin{bmatrix} 1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0& 1\end{bmatrix} \begin{bmatrix} cos(\theta) & -sin(\theta) & 0 \\
sin(\theta) & cos(\theta) & 0 \\
0 & 0& 1\end{bmatrix} \begin{bmatrix} s_x & 0 & 0 \\
0 & s_y & 0 \\
0 & 0& 1\end{bmatrix}  \begin{bmatrix}x\\
y \\
w \end{bmatrix}
```

## Affine transformation

Affine transformation is the combination of linear transformations and translations.

Properties:
* Origin does not necessarily map to origin.
* Lines are still lines.
* Parallel lines remain parallel.
* Ratios are preserved.
* Closed under composition.

```{math}
:label: affine

\begin{bmatrix}x'\\
y' \\
w\end{bmatrix} = \begin{bmatrix} a & b & c \\
d & e & f \\
0 & 0& 1\end{bmatrix} \begin{bmatrix}x\\
y \\
w \end{bmatrix}
```

## Projective transformation

Projective transformation is the combination of affine transformation and projective warps.

Properties:
* Origin does not necessarily map to origin.
* Lines map to lines.
* Parallel lines do not necessarily remain parallel.
* Ratios are not preserved.
* Closed under composition.

```{math}
:label: projective

\begin{bmatrix}x'\\
y' \\
w' \end{bmatrix} = \begin{bmatrix} a & b & c \\
d & e & f \\
g & h & i\end{bmatrix} \begin{bmatrix}x\\
y \\
w \end{bmatrix}
```

Camera performs perspective projection, which is more complex than affine translation.

Summary of 3D - 3D transformation can be found in the image below.

```{figure} /imgs/3d_3d_summary.PNG

---
height: 150px
name: 3d_3d_summary
---

Summary of 3D-3D transformation
```






