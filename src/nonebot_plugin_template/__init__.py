from nonebot.plugin import PluginMetadata, get_plugin_config

from .config import Config

# 插件元数据，填写规范：https://nonebot.dev/docs/next/advanced/plugin-info#%E6%8F%92%E4%BB%B6%E5%85%83%E6%95%B0%E6%8D%AE
__plugin_meta__ = PluginMetadata(
    name="<your_plugin_humanized_name>",
    description="<your_plugin_description>",
    usage="",
    homepage="https://github.com/<your_github>/nonebot-plugin-template",
    type="application",
    config=Config,
    supported_adapters=set(),  # 适配器支持集合
)

plugin_config = get_plugin_config(Config)
