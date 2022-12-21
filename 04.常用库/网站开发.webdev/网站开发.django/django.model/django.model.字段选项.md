---
aliases: 
tags: 
title: django.model.字段选项
date created: 星期三, 十二月 21日 2022, 8:57:45 晚上
date modified: 星期三, 十二月 21日 2022, 9:38:48 晚上
---

# django.model.字段选项

每一种字段都需要指定一些特定的参数。例如 `CharField` 需要接收一个 `max_length` 参数，用以指定数据库存储 `VARCHAR` 数据时用的字节数。

## 通用选项

以下可选的参数是通用的，可以用于任何字段类型：

### null

如果定义为 `True`，Django 将在数据库中存储空值为 NULL。默认为 False。

```ad-hint
避免在基于字符串的字段上使用 `null`，如 `CharField` 和 `TextField`。如果一个基于字符串的字段有 `null=True`，这意味着它有两种可能的`无数据`值：`NULL`、`""(空字符串)`。Django 的惯例是使用空字符串，而不是 NULL。

一个例外是当一个 `CharField` 同时设置了 `unique=True` 和 `blank=True`。在这种情况下，`null=True` 是需要的，以避免在保存具有空白值的多个对象时违反唯一约束。
```

## blank

如果是 True ，该字段允许为空。默认为 False 。

```ad-hint
注意，这与 `null` 不同。 `null` 纯属数据库相关，而 `blank` 则与验证相关。如果一个字段有 `blank=True`，`表单验证`将允许输入一个空值。如果一个字段有 `blank=False`，则该字段为`必填`字段。
```

### choices

一个 `sequence` 本身由正好两个项目的迭代项组成（例如 `[(A, B), (A, B)…]`)，作为该字段的选择。

如果给定了选择，它们会被 ` 模型验证`强制执行，默认的 ` 表单部件`将是一个带有这些选择的选择框，而不是标准的文本字段。

每个元组中的第一个元素是要在模型上设置的实际值，第二个元素是人可读的名称。例如:

```python
YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]
```

一般来说，最好在模型类内部定义选择，并为每个值定义一个合适的名称的常量:

```python
from django.db import models

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}
```

Django 还提供了枚举类型，你可以通过将其子类化来简洁地定义选择：

```python
from django.utils.translation import gettext_lazy as _

class Student(models.Model):

    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        GRADUATE = 'GR', _('Graduate')

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }
```

由于枚举值需要为整数的情况极为常见，Django 提供了一个 `IntegerChoices` 类。例如：

```python
class Card(models.Model):

    class Suit(models.IntegerChoices):
        DIAMOND = 1
        SPADE = 2
        HEART = 3
        CLUB = 4

    suit = models.IntegerField(choices=Suit.choices)
```

也可以使用 [Enum Functional API](https://docs.python.org/3/library/enum.html#functional-api) ，但需要注意的是，标签是自动生成的，如上文所强调的：

```bash
>>> MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
>>> MedalType.choices
[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')]
>>> Place = models.IntegerChoices('Place', 'FIRST SECOND THIRD')
>>> Place.choices
[(1, 'First'), (2, 'Second'), (3, 'Third')]
```

如果你需要支持 int 或 str 以外的具体数据类型，你可以将 Choices 和所需的具体数据类型子类化，例如 date 与 DateField 一起使用：

```python
class MoonLandings(datetime.date, models.Choices):
    APOLLO_11 = 1969, 7, 20, 'Apollo 11 (Eagle)'
    APOLLO_12 = 1969, 11, 19, 'Apollo 12 (Intrepid)'
    APOLLO_14 = 1971, 2, 5, 'Apollo 14 (Antares)'
    APOLLO_15 = 1971, 7, 30, 'Apollo 15 (Falcon)'
    APOLLO_16 = 1972, 4, 21, 'Apollo 16 (Orion)'
    APOLLO_17 = 1972, 12, 11, 'Apollo 17 (Challenger)'
```

### db_column

这个字段要使用的数据库列名。如果没有给出列名，Django 将使用字段名。

### default

该字段的默认值。可以是一个值或者可调用的对象，如果是个可调用对象，每次实例化模型时都会调用该对象。

默认值不能是一个可更改的对象（模型实例、`list`、`set` 等），因为对该对象同一实例的引用将被用作所有新模型实例的缺省值。

如果你想为 JSONField 指定一个默认的 dict，使用一个函数：

```python
def contact_default():
    return {"email": "to1@example.com"}

contact_info = JSONField("ContactInfo", default=contact_default)
```

对于像 `ForeignKey` 这样映射到模型实例的字段，默认应该是它们引用的字段的值（默认是 `pk` 除非 `to_field` 被设置了），而不是模型实例。

当创建新的模型实例且没有为该字段提供值时，使用默认值。当字段是主键时，当字段设置为 ``None`` 时，也使用默认值。

### primary_key

如果设置为 `True` ，将该字段设置为该模型的主键。

如果你没有为模型中的任何字段指定 `primary_key=True`，Django 会自动添加一个字段来保存主键，所以你不需要在任何字段上设置 `primary_key=True`，除非你想覆盖默认主键行为。

`primary_key=True` 意味着 `null=False` 和 `unique=True`。

一个对象只允许有一个主键。

### unique

如果设置为 True，这个字段必须在整个表中保持值唯一。

这是在数据库级别和模型验证中强制执行的。如果你试图保存一个在 unique 字段中存在重复值的模型，模型的 `save()` 方法将引发 `django.db.IntegrityError`。

除了 `ManyToManyField` 和 `OneToOneField` 之外，该选项对所有字段类型有效。

## 字段备注名

除了 `ForeignKey`， `ManyToManyField` 和 `OneToOneField`，任何字段类型都接收一个可选的位置参数 `verbose_name`，如果未指定该参数值， `Django` 会自动使用字段的属性名作为该参数值，并且把下划线转换为空格。

`ForeignKey`, `ManyToManyField` 以及 `OneToOneField` 接收的第一个参数为模型的类名，后面可以添加一个 `verbose_name` 参数：

```python
poll = models.ForeignKey(
    Poll,
    on_delete=models.CASCADE,
    verbose_name="the related poll",
)
```
