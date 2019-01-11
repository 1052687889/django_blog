from django.db import models

# Create your models here.
from django.db import models
from DjangoUeditor.models import UEditorField

class Skill(models.Model):
    name = models.CharField('名称',max_length=20,null=True,default='')

    class Meta:
        verbose_name="技能"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class MyInfo(models.Model):
    zh_name = models.CharField('中文名',max_length=10,null=False,default='黄晔')
    net_name = models.CharField('网名',max_length=10,null=True,default='饕客')
    en_name = models.CharField('英文名',max_length=30,null=True,default='Tate')
    head_img = models.ImageField('头像', upload_to='img/%Y/%m/%d', null=False, default='',blank=True)
    age = models.IntegerField('年龄',default=0)
    sex = models.CharField('性别',max_length=10,null=True,choices=(('male','男'),('female','女')),default='male')
    phone = models.CharField('电话号码',max_length=30,null=True)
    email = models.EmailField('邮箱',null=True)
    addr = models.CharField('地址',max_length=300,null=True)
    wechat = models.ImageField('微信',upload_to='img/%Y/%m/%d', null=False, default='',blank=True)
    describe = UEditorField(verbose_name='自我描述',
                            width=700,
                            height=400,
                            toolbars='full',
                            imagePath='ueditor/images/',
                            filePath='ueditor/files/',
                            upload_settings={'imageMaxSizing':1024000},
                            default='')
    resume = models.URLField('简历',max_length=200,null=True)
    skills = models.ManyToManyField(Skill,verbose_name='技能',through='Level')
    num = models.IntegerField('点赞数', default=0)

    class Meta:
        verbose_name="关于我"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.zh_name


class Level(models.Model):
    myinfo = models.ForeignKey(MyInfo,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    score = models.IntegerField('分数',default=0)

    class Meta:
        verbose_name="技能水平"
        verbose_name_plural=verbose_name

    def __str__(self):
        return str(self.myinfo) + ' ' + str(self.skill) + ' ' + str(self.score)










