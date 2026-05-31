---
title: Mean Squared Error
description: Concept Note for Mean Squared Error
tags:
  - mse
  - loss-function
  - regression
updated_date: 2026-05-11
---

# Mean Squared Error

The Mean Squared Error (MSE) measures the **average squared difference between predicted values and actual values**.

## Formula

- Compute how wrong each prediction is.
- Square each error.
- Average all squared errors.

$$
\mathrm{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
$$

## Penalization on large errors and small errors

Since MSE is a squared error, the square of small errors results in a smaller value and the square of larger numbers results in a larger value. Hence, MSE penalizes large errors more than small errors and thus is **more sensitive to outliers**.

## MSE Loss Curve Significance and Shape

The loss curve is a parabola.

$$
L(e)=e^2
$$

Properties:

- Minimum at $e=0$, because when error is 0, loss is 0. This is the global minimum.
- Symmetric around zero - Positive and negative errors are penalized equally
- Larger errors receive quadratically larger penalties
- Smooth and differentiable with gradient $\frac{dL}{de}=2e$

## Why is MSE a popular choice for loss functions

- **Easy to optimize** - MSE is continuous, smooth, differentiable everywhere, hence gradient descent is stable and efficient.
- **Strong mathematical properties** - The squared term leads to convex optimization problems for many linear models
- **Penalizes catastrophic mistakes** - Large errors receive much larger penalties. This is desirable when large mistakes are particularly costly.
- **Widely supported and understood** - Many algorithms, libraries, and theoretical results are built around MSE. It often serves as the default baseline for regression problems.

## When is MSE not ideal

- Data contains many outliers - Since MSE penalizes larger errors more, it can cause models to fit more closely around outliers.
- Robustness is more important than aggressively reducing large errors - To achieve robustness with datasets having outliers, MSE is not the preferred choice

## Implementing MSE from scratch

Following implementation of MSE is in Python, primarily using the `numpy` library

```python
def mean_squared_error(y_true, y_pred):
    mse = 0
    for y_i, y_hat_i in zip(y_true, y_pred):
        mse += (y_i - y_hat_i)**2
    mse = mse / len(y_true) # Need to take average
    return mse
```

Using `for` loops does not scale very well when working with very large datasets. We can optimize the calculation further by using vector calculations.

```python
def mean_squared_error(y_true, y_pred):
    mse = np.mean((y_true - y_pred) ** 2)
    return mse
```

When training custom deep learning models, PyTorch is one of the most popular frameworks. We can implement the optimized version of MSE as follows:

```python
# Writing from scratch
def mean_squared_error(y_true, y_pred):
    mse = torch.mean((y_true - y_pred) ** 2)

# PyTorch's inbuilt torch.nn.MSELoss()
criterion = torch.nn.MSELoss()
torch_mse = criterion(y_pred, y_true)
```
