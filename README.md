# g66-python-prictice

Yixiaohan/show-me-the-code中的python练习题

# 题目列表

**第 0001 题：** 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

**第 0002 题:** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

**第 0003 题：** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。

**第 0004 题：** 任一个英文的纯文本文件，统计其中的单词出现的个数。

**第 0005 题：** 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。（调整为2400 * 1080分辩率，适应当前移动端app）

**第 0006 题：** 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

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

## 0006.统计单词出现次数

目录下文件遍历

调用练习3中的count_word函数，统计目录下所有txt文件中单词出现的次数，返回的是一个排序好的字典列表

1. 使用os.listdir()获取目录下文件列表，files.lower().endswith(('.txt'))判断文件是否为txt文件
2. 使用os.path.join()拼接文件路径
3. 数组切片[:5]获取前5个元素
