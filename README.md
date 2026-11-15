# 珍珠网站产品详情页图片生成skill

基于真实产品照片制作珍珠首饰封面、白底三视图、细节图、礼盒俯拍、佩戴图、生活环境图、尺子比例参考和证书遮号副本。

## 使用

将本目录作为 skill 导入支持 SKILL.md 的工具，或让助手读取 [SKILL.md](SKILL.md)。提供该件产品原图、类别、已确认尺寸和要制作的图片类型；先审核成图，再另行授权网站配置。无自动上传、发布或API调用。

几何检查脚本需要 Python 3 与 Pillow：

```sh
pip install Pillow
python scripts/check_cover_manifest.py manifest.json
```

输入格式与限制见 [封面规则](references/cover-geometry.md) 和脚本注释。脚本只校验人工提供的边界框与尺寸，不证明产品真实性。

本公开版仅含通用规则和校验代码，不含客户照片、证书、私人目录或内部资料引用。图像制作遵循实物事实，不凭空添加材质、角度结构或尺寸。
