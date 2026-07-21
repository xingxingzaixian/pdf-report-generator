import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'PDF Report Generator',
  description: '一个强大、灵活的 PDF 报告生成系统',
  base: '/',
  ignoreDeadLinks: [
    /localhost/,
    /advanced-features/,
    /advanced\/index/
  ],

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }]
  ],

  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'PDF Report Generator',

    nav: [
      { text: '指南', link: '/guide/what-is-pdf-report-generator', activeMatch: '/guide/' },
      { text: 'API 参考', link: '/api/', activeMatch: '/api/' },
      { text: '示例', link: '/examples/', activeMatch: '/examples/' },
      {
        text: '相关链接',
        items: [
          { text: 'GitHub', link: 'https://github.com/your-org/pdf-report-generator' },
          { text: 'PyPI', link: 'https://pypi.org/project/pdf-report-generator/' }
        ]
      }
    ],

    sidebar: {
      '/guide/': [
        {
          text: '简介',
          items: [
            { text: '什么是 PDF Report Generator', link: '/guide/what-is-pdf-report-generator' },
            { text: '特性一览', link: '/guide/features' }
          ]
        },
        {
          text: '快速开始',
          items: [
            { text: '安装', link: '/guide/installation' },
            { text: '第一个报告', link: '/guide/first-report' },
            { text: 'Python 库使用', link: '/guide/usage-python' },
            { text: 'Web API 使用', link: '/guide/usage-api' }
          ]
        },
        {
          text: '核心概念',
          items: [
            { text: '配置结构总览', link: '/guide/configuration-overview' },
            { text: '元数据配置', link: '/guide/metadata' },
            { text: '样式系统', link: '/guide/styles' },
            { text: '元素系统', link: '/guide/elements' },
            { text: '数据源', link: '/guide/data-sources' }
          ]
        },
        {
          text: '进阶',
          items: [
            { text: '数据管道', link: '/guide/pipeline' },
            { text: '模板系统', link: '/guide/templates' },
            { text: '部署', link: '/guide/deployment' }
          ]
        }
      ],

      '/api/': [
        {
          text: 'API 参考',
          items: [
            { text: '概览', link: '/api/' },
            { text: 'PDFReportGenerator', link: '/api/pdf-report-generator' },
            { text: 'Web API 端点', link: '/api/web-api' },
            { text: '配置 Schema', link: '/api/configuration-schema' }
          ]
        }
      ],

      '/advanced/': [
        {
          text: '高级功能',
          items: [
            { text: '页眉页脚', link: '/advanced/headers-footers' },
            { text: '页码格式', link: '/advanced/page-numbers' },
            { text: '自动目录', link: '/advanced/table-of-contents' },
            { text: '封面页', link: '/advanced/cover-pages' },
            { text: '表格合并', link: '/advanced/table-merging' },
            { text: '图片处理', link: '/advanced/images' },
            { text: '中文字体', link: '/advanced/chinese-fonts' },
            { text: '条件渲染', link: '/advanced/conditional-rendering' },
            { text: '超链接与书签', link: '/advanced/bookmarks-links' }
          ]
        }
      ],

      '/examples/': [
        {
          text: '示例',
          items: [
            { text: '总览', link: '/examples/' },
            { text: '基础示例', link: '/examples/basics' },
            { text: '数据源示例', link: '/examples/data-sources' },
            { text: '图表示例', link: '/examples/charts' },
            { text: '综合示例', link: '/examples/comprehensive' },
            { text: 'Pipeline 示例', link: '/examples/pipeline' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/your-org/pdf-report-generator' }
    ],

    editLink: {
      pattern: 'https://github.com/your-org/pdf-report-generator/edit/main/website/docs/:path'
    },

    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024 PDF Report Team'
    },

    search: {
      provider: 'local'
    },

    outline: {
      level: [2, 3],
      label: '页面导航'
    }
  }
})
