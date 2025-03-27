# g66-python-prictice

Yixiaohan/show-me-the-code中的python练习题

# 题目列表

**第 0001 题：** 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

**第 0002 题:** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

**第 0003 题：** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。

**第 0004 题：** 任一个英文的纯文本文件，统计其中的单词出现的个数。

**第 0005 题：** 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。（调整为2400 * 1080分辩率，适应当前移动端app）


# 方法总结



## 0005.处理图片


以下是这段代码中用到的库和方法的总结：

---

1. **`os` 模块**

- **`os.listdir(path)`**：

  - 用于列出指定路径下的所有文件和文件夹。
  - 在代码中用于遍历文件夹 `i_path` 下的所有文件。
  - 示例：
    ```python
    for image in os.listdir(i_path):
    ```
- **`os.path.join(path, *paths)`**：

  - 用于拼接路径，生成完整的文件路径。
  - 在代码中用于将文件夹路径和文件名拼接成完整的图片路径。
  - 示例：
    ```python
    image_path = os.path.join(i_path, image)
    ```

---

2. **`Pillow` 库（`PIL`）**

- **`PIL.Image.open(fp)`**：

  - 用于打开图片文件，返回一个 `Image` 对象。
  - 在代码中用于打开指定路径的图片文件。
  - 示例：
    ```python
    with PILImage.open(image_path) as image:
    ```
- **`Image.resize(size, resample)`**：

  - 用于调整图片大小。
  - 参数：
    - `size`：目标尺寸，格式为 `(宽度, 高度)`。
    - `resample`：重采样过滤器，用于控制缩放质量。
      - 在代码中使用了 `PILImage.Resampling.LANCZOS`，这是一个高质量的重采样过滤器。
  - 示例：
    ```python
    resized_image = image.resize((target_width, target_height), PILImage.Resampling.LANCZOS)
    ```
- **`Image.save(fp, format)`**：

  - 用于将图片保存到指定路径。
  - 参数：
    - `fp`：保存路径。
    - `format`：图片格式（如 `"JPEG"`）。
  - 示例：
    ```python
    resized_image.save(resized_path, "JPEG")
    ```

---

3. **代码逻辑中的方法调用**

- **`resize_image(image_path, target_width, target_height)`**：
  - 自定义的函数，用于调整图片大小并保存到新的路径。
  - 调用了以下方法：
    - `PILImage.open()`：打开图片。
    - `Image.resize()`：调整图片大小。
    - `Image.save()`：保存调整后的图片。

---

4. **异常处理**

- **`try...except` 块**：
  - 用于捕获和处理运行时可能发生的异常。
  - 在代码中用于捕获图片处理过程中可能发生的错误，并打印错误信息。
  - 示例：
    ```python
    try:
        resize_image(image_path, 2400, 1080)
        print(f"图片 {image} 已调整大小！")
    except Exception as e:
        print(f"调整图片 {image} 大小时发生错误: {e}")
    ```

---

总结

这段代码使用了以下库和方法：

1. **`os` 模块**：

   - `os.listdir()`：列出文件夹内容。
   - `os.path.join()`：拼接路径。
2. **`Pillow` 库**：

   - `PIL.Image.open()`：打开图片。
   - `Image.resize()`：调整图片大小。
   - `Image.save()`：保存图片。
3. **异常处理**：

   - `try...except`：捕获并处理图片处理过程中的错误。

这些方法共同实现了从文件夹中读取图片、调整图片大小并保存的功能，同时对可能的错误进行了处理。
