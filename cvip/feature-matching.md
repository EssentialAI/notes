# Feature Matching

Keep in mind that the problem at hand is the 2D $\rightarrow$ 3D reconstruction problem. 

* The previous pages discuss about using an image patch to find the best candidates for the 8 corresponding points between left and right images to find the <span class = 'high'>Fundamental Matrix.</span>

* We use the Harris matrix $H$ to find the potential best candidates for correspondence between the left and right images. Using eigen values of the matrix $H$ makes the computation of corner detection much simpler. This leads to the Harris Operator $f$ that is defined [here](image-features.html#the-harris-operator).
* However, the harris operator is not scale invariant. To find the automatic size of the patch that would best find the corner (candidates for correspondence). This is  grid search problem.
* SIFT features provide a better alternative to the above grid search by converting the rectangular image patch to a circle and using gradient values at each pixel. These gradients are represented in the form of histograms by rotating the circle the gradient values are matched between the patches.

<span class='high'>This leads us to the feature matching problem. Finding what candidate in the left image maps to what candidate in the right image.</span>

```{figure} /imgs/feature-matching.PNG

---
height: 150px
name: feature-matching
---

Feature Matching
```

```{note}
Even though the features can be independent (or a good candidate) there could be more than one match for a feature in the left image to feature in the right image.
```

To overcome this problem, we pick two matches for a given feature in the left image and maintain a score function to find the relative difference between the matched features. Refer to the feature matching example for the window fencing from slides.

```{note}
Harris corner detector tells if a feature is good candidate for correspondence matching or not, it does not say if the feature is unique or no.
```

Performance of feature matching is measured in terms of true positives/false positives true negatives/false negatives.

```{figure} /imgs/performance.PNG

---
height: 150px
name: performance
---

Performance of Feature Matching
```


### Properties of SIFT features

* Can handle changes in viewpoint
  * Upto about 60 degree out of plane rotation
* Can handle significant changes in illumination
* Fast and efficient - can run in real time
* Lots of code available.


# RANSAC

This is a randomized algorithm. We randomly pick a random sample of points and define a <span class = 'high'>loss function</span>. We choose points that minimize this loss function.

This is very close to the <span class = 'high'>Model fitting</span> problem in Machine Learning. For example, least squares. Refer Linear Regression for more information.

For Linear Regression, we need precisely two training points to find the slope $a$ and intercept $b$.

Here, in the case of Fundamental matrix, we have $ x_r' F x_l $. We need 8 corresponding points. In this case the fundamental matrix is a parametric model. To achieve the best curve that best captures the geometry of points, we define a loss function and minimize the loss function.

In case of Linear Regression, this loss function is the Sum of Squared Residuals.

Ransac automatically takes care of the noise in the training samples.

```{note}
For more details about RANSAC refer [here](https://www.youtube.com/watch?v=9D5rrtCC_E0) and [here](http://www.cse.yorku.ca/~kosta/CompVis_Notes/ransac.pdf)
```

In general,

```{math}
:label: ransac

p = 1-(1-w^n)^k
```

where,
* p = probability of selecting inliers
* w = ratio of inliers to total # of points
* n = minimum # of points required (for line=2, circle = 3)
* k = # of iterations

