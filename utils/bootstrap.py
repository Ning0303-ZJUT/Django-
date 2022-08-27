from django import forms

class Bootstrap:
    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #循环ModelForm 中的所有字段，给每个字段插件设置
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            #字段中有属性则保留，没有属性则添加
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {
                    "class": 'form-control',
                    'placeholder': field.label
                }

class BootstrapModelForm(Bootstrap, forms.ModelForm):
    pass

class BootstrapForm(Bootstrap, forms.Form):
    pass