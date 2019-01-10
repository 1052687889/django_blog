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
    # describe = models.TextField('自我描述',null=True)
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

    zh_name_useful = models.BooleanField('中文名字是否有效',default=True)
    net_name_useful = models.BooleanField('网名是否有效',default=True)
    en_name_useful = models.BooleanField('英文名字是否有效',default=True)
    head_img_useful = models.BooleanField('头像是否有效', default=True)
    age_useful = models.BooleanField('年龄是否有效',default=True)
    sex_useful = models.BooleanField('性别是否有效',default=True)
    phone_useful = models.BooleanField('电话号码是否有效',default=True)
    email_useful = models.BooleanField('邮箱是否有效',default=True)
    addr_useful = models.BooleanField('地址是否有效',default=True)
    wechat_useful = models.BooleanField('微信是否有效',default=True)
    describe_useful = models.BooleanField('自我描述是否有效',default=True)
    resume_useful = models.BooleanField('简历是否有效',default=True)

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










