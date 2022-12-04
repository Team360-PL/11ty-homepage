# Homepage for Team360

New homepage for Team360.

## Install and run locally

1. check out this repository
2. run `npm install` once
3. run `npm start` to launch development server (running on port 8081)

## Edit files

* Blog articles, news, announcements etc. are stored in `posts`
* Static pages (i.e. everything which is not a post) are found in `pages`

## Contributing articles

Articles should use [CommonMark](https://commonmark.org/help/) markdown syntax and start with a header separated by `---`. You can use the file [posts/article-template.md](posts/article-template.md) as a template. The following fields can be present in the header:

```yaml
---
title: Full title of the article
short: (optional) Short title
lead: (optional) Descriptive short summary
author: Author of the article
date: 2022-10-25
tags:
    - events
    - meetups
coverImage: Image to be used as cover, located in img folder
coverImageCredits: Any credits to be shown for the cover image
---
```

Every article should use at least one of the following tags. Nested tags below should be used in combination with the corresponding parent tag.

* bno
  * wesolino
  * ctz
  * ... other tags related to orienteering
* biegi
  * wbg
  * jbg
  * zbg
  * ... other tags related to regular running competitions
* trening
  * wf
* tutorial
  * początkujący
  * pro-tip
  * ...
* faq
