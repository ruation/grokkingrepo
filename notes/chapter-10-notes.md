# k-Nearest Neighbors (KNN)

k-Nearest Neighbors (KNN) is a **supervised machine learning algorithm** used for **classification** and **regression**.

The algorithm predicts the label or value of a data point by looking at the **k closest data points** in the dataset.

---

## Key Idea

Objects that are **similar tend to be close to each other** in the feature space.

To make a prediction:

1. Choose a value for **k** (number of neighbors).
2. Calculate the **distance** between the new data point and all other points.
3. Select the **k closest neighbors**.
4. Use those neighbors to determine the prediction.

For classification, the algorithm usually uses **majority voting**.

---

## Example

Suppose we want to classify a fruit based on its features:

| Weight | Color | Label |
|------|------|------|
| 150g | Red | Apple |
| 170g | Red | Apple |
| 140g | Yellow | Lemon |

If a new fruit is close to the **apple points**, the algorithm will classify it as an **apple**.

---

## Choosing K

The value of **k** determines how many neighbors influence the decision.

- Small **k** → more sensitive to noise
- Large **k** → smoother predictions but may ignore local patterns

A common choice is an **odd number** to avoid ties.

---

## Distance Metrics

To measure similarity, KNN uses a **distance function**.

Common choices include:

- **Euclidean distance**
- **Manhattan distance**
- **Cosine similarity**

Example (Euclidean distance):

distance = √((x2 - x1)² + (y2 - y1)²)


---

## Advantages

- Simple to understand and implement
- No training phase required
- Works well with small datasets

---

## Limitations

- Slow for large datasets
- Requires storing the entire dataset
- Performance depends on the choice of **k** and the distance metric

---

## Time Complexity

Prediction time:

O(n)


Where **n** is the number of data points in the dataset.

---

## Summary

k-Nearest Neighbors (KNN):

- A **supervised learning algorithm**
- Classifies data based on the **k closest neighbors**
- Uses **distance metrics** to measure similarity
- Simple but computationally expensive for large datasets
