from django import forms


class IDPhotoForm(forms.Form):
    image = forms.ImageField()
    width = forms.IntegerField()
    height = forms.IntegerField()
    matting_model = forms.Select()
    detect_model = forms.Select()
    hd = forms.BooleanField()
    dpi = forms.IntegerField()
    face_align = forms.BooleanField()
    head_measure_ratio = forms.FloatField()
    head_height_ratio = forms.FloatField()
    top_distance_max = forms.FloatField()
    top_distance_min = forms.FloatField()


class PhotoMattingForm(forms.Form):
    image = forms.ImageField()
    matting_model = forms.Select()
    dpi = forms.IntegerField()


class PhotoResizeForm(forms.Form):
    image = forms.ImageField()
    matting_model = forms.Select()
    dpi = forms.IntegerField()


class PhotoCropForm(forms.Form):
    image = forms.ImageField()
    width = forms.IntegerField()
    height = forms.IntegerField()
    detect_model = forms.Select()
    hd = forms.BooleanField()
    dpi = forms.IntegerField()
    face_align = forms.BooleanField()
    head_measure_ratio = forms.FloatField()
    head_height_ratio = forms.FloatField()
    top_distance_max = forms.FloatField()
    top_distance_min = forms.FloatField()
