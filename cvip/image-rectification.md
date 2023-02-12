# How to rectify two cameras?

**Recap**

The entire aim of rectification is to perform the 2D $\rightarrow$ 3D mapping from an image coordinate to a 3D real world point. This is required to ESTIMATE the true depth information of a point in space. <span class = 'high'>We have discussed, how this 2D $\rightarrow$ 3D mapping is not possible by using a single image and we require a minimum of 2 images.</span>

With two images, for depth estimation, we make use of <span class = 'high'>epipolar geometry.</span>

```{note}

Given two image coordinates $x_l$ and $x_r$ of the same point from left and right cameras, can we perform the 2D to 3D mapping to estimate the depth between points in the real world?

Better yet, given a point $x_l$ in the left camera, can we find the corresponding point $x_r$ in the right camera? Multi-view geometry problem.
```

For pixel matching between two cameras, we need to first rectify the images, such that the pixel search between left and right images becomes a linear search.

To perform this rectification, we need to rotate cameras such that the image planes are parallel to each other.

```{figure} /imgs/epipolar.PNG

---
height: 150px
name: epipolar
---

Epipolar Geometry
```

$P \rightarrow$ Point in real world. $[X,Y,Z]^T$

$ P_l \rightarrow $ Position of $P$ as seen from left camera. ${P_l}_{3 \times 1}$

$ P_r \rightarrow $ Position of $P$ as seen from right camera. ${P_r}_{3 \times 1}$

$ T \rightarrow $ Baseline between the camera $C_l$ and $C_r$.

Using the co-planarity constraint, we can find a relation between the point in the left camera and the point in the right camera.

```{figure} /imgs/co-planarity-constraint.PNG

---
height: 150px
name: co-planar
---

Using coplanarity constraint to find the relation between $P_l$ and $P_r$
```

## The Essential Matrix

```{figure} /imgs/essential-matrix.PNG

---
height: 150px
name: essential matrix
---

Essential Matrix
```

The vector $T = [T_x, T_y, T_z]^T$ is the relative distance (in 3D coordinates) between the left and the right cameras.

The above figure gives us the relations:

```{math}
:label: essential-matrix1

E = RS
```

```{math}
:label: essential-matrix

P_r^TEP_l = 0
```

If you look at the above equation carefully, the matrix $E$ is not unique. The above equation is satisfied even if we use $2E$ or $nE$ instead of $E$. This means $E$ is not unique.

```{admonition} Why is $E$ not unique?
:class: tip

This is due to the fact what the baseline $T$ provides us with the information of the direction between cameras, but does not provide the actual distance between the cameras. The equation $P_r^TRT \times P_l=0$ is satisfied for any integer multiple of $T$.
```

$E$ has only 5 degrees of freedom.

Using $P_r^TEP_l = 0$ we cannot find the exact relation between $P_l$ and $P_r$. The equation has infinite solutions.

## The Fundamental Matrix

<span class = 'high'>An important detail to observe here is that, $P_l$ and $P_r$ are 3D locations as seen from left and right cameras, respectively.</span>

<span class = 'high'>Fundamental matrix captures the relation between the 2D image coordinates.</span>

```{figure} /imgs/fundamental-matrix.PNG

---
height: 150px
name: fundamental matrix
---

Fundamental Matrix
```

In the above figure $M_l$ and $M_r$ are the intrinsic parameter matrices of left and right cameras respectively.

```{admonition} What is the use of Essential and Fundamental matrices?
:class: tip

The Essential Matrix is responsible for translating and rotating the cameras such that both the cameras are aligned with each other. It provides the constraint equation between the 3D points $P_l$ and $P_r$.

The Fundamental Matrix is responsible for mapping the above 3D points onto the pixel locations $x_l$ and $x_r$ on the virtual image plane such that the epipolar lines are aligned. This means the correspondence problem now becomes a linear search.

This is how essential matrix and fundamental matrix perform image rectification.
```

Fundamental matrix knows the intrinsic parameters of both cameras, and the extrinsic parameters from the Essential Matrix. However, fundamental matrix also does not know the distance between the cameras. <span class = 'high'>Fundamental Matrix is not unique.</span>

Even if you know $x_l$, you still cannot find the coordinates of $x_r$, using the fundamental matrix.

This perfectly matches with the <span class = 'high'>correspondence problem.</span> The Fundamental matrix helps us perform the DEPTH ESTIMATION, by boiling down the problem to correspondence problem. This problem shall be discussed in the future sections.

```{note}

E $\rightarrow$ 5 Degrees of freedom

rank(E) $\rightarrow$ 2

E $\rightarrow$ extrinsic parameters

<hr>

F $\rightarrow$ 7 Degrees of freedom

rank(F) $\rightarrow$ 2

F $\rightarrow$ extrinsic parameters from E and intrinsic parameters of both the cameras.

$x_l$ and $x_r$ are the homogeneous coordinates of the 2D point. In the form of $s[X,Y,1]^T$.
```

# Correspondence problem using Fundamental Matrix

```{math}
:label: correspondence

\begin{bmatrix}
x_i \\
y_i \\
1 
\end{bmatrix}^T \begin{bmatrix}
f_{11} & f_{12} & f_{13}  \\
f_{21} & f_{22} & f_{23}   \\
f_{31} & f_{32} & f_{33} 
\end{bmatrix}
\begin{bmatrix}
x_{i}' \\
y_{i}' \\
1 
\end{bmatrix}=0
```

In the above equation, if we find the Fundamental matrix, we can find the relation between $x_l$ and $x_r$. This means, we can map any 2D image coordinate from one camera to a 2D image coordinate on another camera. This would solve the depth estimation and the 2D $\rightarrow$ 3D.

**Finding $F$ can be solved if we find 8 corresponding points from left camera and right camera.**











<!-- Intuitively, to rectify two cameras with each other, we need to rotate the cameras.
1. Rotate right (or left) camera to be in the same pose as left (or right) camera.
2. Then rotate both cameras to be parallel to the baseline.

Before contuining to image rectification, lets define some notations.

$x_1$ is the object location (usually a point), located in image1.

$x_2$ is the object location (usually a point), located in image2.

Before solving the correspondence problem, we are required to rotate the cameras to be in line with eachother.

Let $X = [X,Y,Z]^T$ be the world coordinate of the image coordinates, $x_1$ and $x_2$.

From {eq}`projection` we know that the image location of a point is found by the dot product of intrinsic and extrinsic camera parameters.

$$
x_1 = KR_1X = R_1^{-1}K^{-1}x_1
$$

$$
x_2 = KR_1X = K R_2R_1^{-1}K^{-1}*x_1
$$

This gives us a representation of $x_2$ in terms of $x_1$ after rotation.

```{math}
:label: recitification

x_2 = Hx_1
```

$$
H = KR_2R_1^{-1}K^{-1}
$$

Here in the above case, both cameras are considered to have the same intrinsic parameter matrix $K$. Else, $K_1$, $K_2$.

In short, to find the matrix $H$, we need to know:
1. Intrinsic parameters of the cameras
2. The pose of the camera.

The translation is considered to be $0$ here.

## Fundamental matrix

<span class = 'high'>The epipolar geometry is the intrinsic projective geometry between two views. It is independent of scene structure, and only depends on the internal parameters and the relative pose.</span>

The fundamental matrix $F$ encapsulates this intrinsic geometry. It is a $3 \times 3$ matrix of <span class ='high'>rank 2</span>. If a point in a 3-space $X$ is images as $x_1$ in the first view and $x_2$ in the second, then the image points satisfy the relation:

```{math}
:label: fundamental
x_2^TFx = 0
```

### Calculating fundamental matrix

$$
P_r = R(P_l-T)
$$ -->






