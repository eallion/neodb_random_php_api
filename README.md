# Self-hosted NeoDB 随机电影

### PHP API

`/api` 目录提供一个简单的自部署 PHP 版本 API。数据来自 NeoDB 的缓存。

**说明：**
数据范围只包含 `IMDB Top250` 和 `豆瓣 Top250` 和混合合集，共 406 部电影。
影片名单参见：https://neodb.social/collection/5BJEo6UQs8KbAivjOUpAcb

#### Parameter

- `/` 返回纯文本的 UUID
- `?type=json` 随机返回一部影片的完整信息
- `?uuid={UUID}` 返回指定的 UUID 的影片信息

#### Request

- GET: `https://example-api-host.com/api-endpoint`

Response:

```txt
6SAqdyMEu3kGepBN0mHZAr
```

- GET: `https://example-api-host.com/api-endpoint?type=json`

Response: 同下

- GET: `https://example-api-host.com/api-endpoint?uuid=6SAqdyMEu3kGepBN0mHZAr`

```json
{
  "id": "https://neodb.social/movie/6SAqdyMEu3kGepBN0mHZAr",
  "type": "Movie",
  "uuid": "6SAqdyMEu3kGepBN0mHZAr",
  "url": "/movie/6SAqdyMEu3kGepBN0mHZAr",
  "api_url": "/api/movie/6SAqdyMEu3kGepBN0mHZAr",
  "category": "movie",
  "parent_uuid": null,
  "display_title": "肖申克的救赎",
  "external_resources": [
    {
      "url": "https://www.themoviedb.org/movie/278"
    },
    {
      "url": "https://www.imdb.com/title/tt0111161/"
    },
    {
      "url": "https://movie.douban.com/subject/1292052/"
    }
  ],
  "title": "肖申克的救赎",
  "description": "一场谋杀案使银行家安迪（蒂姆•罗宾斯 Tim Robbins 饰）蒙冤入狱，谋杀妻子及其情人的指控将囚禁他终生。在肖申克监狱的首次现身就让监狱“大哥”瑞德（摩根•弗里曼 Morgan Freeman 饰）对他另眼相看。瑞德帮助他搞到一把石锤和一幅女明星海报，两人渐成患难 之交。很快，安迪在监狱里大显其才，担当监狱图书管理员，并利用自己的金融知识帮助监狱官避税，引起了典狱长的注意，被招致麾下帮助典狱长洗黑钱。偶然一次，他得知一名新入狱的小偷能够作证帮他洗脱谋杀罪。燃起一丝希望的安迪找到了典狱长，希望他能帮自己翻案。阴险伪善的狱长假装答应安迪，背后却派人杀死小偷，让他唯一能合法出狱的希望泯灭。沮丧的安迪并没有绝望，在一个电闪雷鸣的风雨夜，一场暗藏几十年的越狱计划让他自我救赎，重获自由！老朋友瑞德在他的鼓舞和帮助下，也勇敢地奔向自由。\n本片获得1995年奥斯卡10项提名，以及金球奖、土星奖等多项提名。",
  "localized_title": [
    {
      "lang": "zh-cn",
      "text": "肖申克的救赎"
    },
    {
      "lang": "en",
      "text": "The Shawshank Redemption"
    },
    {
      "lang": "zh-cn",
      "text": "月黑高飞(港)"
    },
    {
      "lang": "zh-cn",
      "text": "刺激1995(台)"
    },
    {
      "lang": "zh-cn",
      "text": "地狱诺言"
    },
    {
      "lang": "zh-cn",
      "text": "铁窗岁月"
    },
    {
      "lang": "zh-cn",
      "text": "消香克的救赎"
    }
  ],
  "localized_description": [
    {
      "lang": "zh-cn",
      "text": "一场谋杀案使银行家安迪（蒂姆•罗宾斯 Tim Robbins 饰）蒙冤入狱，谋杀妻子及其情人的指控将囚禁他终生。在肖申克监狱的首次现身就让监狱“大哥”瑞德（摩根•弗里曼 Morgan Freeman 饰）对他另眼相看。瑞德帮助他搞到一把石锤和一幅女明星海报，两人渐成患难 之交。很快，安迪在监狱里大显其才，担当监狱图书管理员，并利用自己的金融知识帮助监狱官避税，引起了典狱长的注意，被招致麾下帮助典狱长洗黑钱。偶然一次，他得知一名新入狱的小偷能够作证帮他洗脱谋杀罪。燃起一丝希望的安迪找到了典狱长，希望他能帮自己翻案。阴险伪善的狱长假装答应安迪，背后却派人杀死小偷，让他唯一能合法出狱的希望泯灭。沮丧的安迪并没有绝望，在一个电闪雷鸣的风雨夜，一场暗藏几十年的越狱计划让他自我救赎，重获自由！老朋友瑞德在他的鼓舞和帮助下，也勇敢地奔向自由。\n本片获得1995年奥斯卡10项提名，以及金球奖、土星奖等多项提名。"
    }
  ],
  "cover_image_url": "https://neodb.social/m/movie/2021/09/14e5043627-8e2d-43c0-a6cc-a8e05d8115d3.jpg",
  "rating": 9.4,
  "rating_count": 2413,
  "brief": "一场谋杀案使银行家安迪（蒂姆•罗宾斯 Tim Robbins 饰）蒙冤入狱，谋杀妻子及其情人的指控将囚禁他终生。在肖申克监狱的首次现身就让监狱“大哥”瑞德（摩根•弗里曼 Morgan Freeman 饰）对他另眼相看。瑞德帮助他搞到一把石锤和一幅女明星海报，两人渐成患难 之交。很快，安迪在监狱里大显其才，担当监狱图书管理员，并利用自己的金融知识帮助监狱官避税，引起了典狱长的注意，被招致麾下帮助典狱长洗黑钱。偶然一次，他得知一名新入狱的小偷能够作证帮他洗脱谋杀罪。燃起一丝希望的安迪找到了典狱长，希望他能帮自己翻案。阴险伪善的狱长假装答应安迪，背后却派人杀死小偷，让他唯一能合法出狱的希望泯灭。沮丧的安迪并没有绝望，在一个电闪雷鸣的风雨夜，一场暗藏几十年的越狱计划让他自我救赎，重获自由！老朋友瑞德在他的鼓舞和帮助下，也勇敢地奔向自由。\n本片获得1995年奥斯卡10项提名，以及金球奖、土星奖等多项提名。",
  "orig_title": "The Shawshank Redemption",
  "other_title": [
    "月黑高飞(港)",
    "刺激1995(台)",
    "地狱诺言",
    "铁窗岁月",
    "消香克的救赎"
  ],
  "director": [
    "弗兰克·德拉邦特"
  ],
  "playwright": [
    "弗兰克·德拉邦特",
    "斯蒂芬·金"
  ],
  "actor": [
    "蒂姆·罗宾斯",
    "摩根·弗里曼",
    "鲍勃·冈顿",
    "威廉姆·赛德勒",
    "克兰西·布朗",
    "吉尔·贝罗斯",
    "马克·罗斯顿",
    "詹姆斯·惠特摩",
    "杰弗里·德曼",
    "拉里·布兰登伯格",
    "尼尔·吉恩托利",
    "布赖恩·利比",
    "大卫·普罗瓦尔",
    "约瑟夫·劳格诺",
    "祖德·塞克利拉",
    "保罗·麦克兰尼",
    "芮妮·布莱恩",
    "阿方索·弗里曼",
    "V·J·福斯特",
    "弗兰克·梅德拉诺",
    "马克·迈尔斯",
    "尼尔·萨默斯",
    "耐德·巴拉米",
    "布赖恩·戴拉特",
    "唐·麦克马纳斯"
  ],
  "genre": [
    "Drama",
    "Crime"
  ],
  "language": [
    "英语"
  ],
  "area": [
    "美国"
  ],
  "year": 1994,
  "site": "",
  "duration": "142分钟",
  "imdb": "tt0111161"
}
```
