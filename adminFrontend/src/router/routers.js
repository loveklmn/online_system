import Main from '@/view/main'
import parentView from '@/components/parent-view'

/**
 * iview-admin中meta除了原生参数外可配置的参数:
 * meta: {
 *  hideInMenu: (false) 设为true后在左侧菜单不会显示该页面选项
 *  notCache: (false) 设为true后页面不会缓存
 *  access: (null) 可访问该页面的权限数组，当前路由设置的权限会影响子路由
 *  icon: (-) 该页面在左侧菜单、面包屑和标签导航处显示的图标，如果是自定义图标，需要在图标名称前加下划线'_'
 * }
 */

export default [
  {
    path: '/login',
    name: 'login',
    meta: {
      title: 'Login - 登录',
      hideInMenu: true
    },
    component: () => import('@/view/login/login.vue')
  },
  {
    path: '/',
    name: '_home',
    redirect: '/home',
    component: Main,
    meta: {
      hideInMenu: true,
      notCache: true
    },
    children: [
      {
        path: '/home',
        name: 'home',
        meta: {
          hideInMenu: true,
          title: '弗恩英语后台管理系统',
          notCache: true
        },
        component: () => import('@/view/single-page/home')
      }
    ]
  },
  {
    path: '/manage_user_page',
    name: 'manage_user',
    meta: {
      icon: 'logo-buffer',
      title: '用户权限管理'
    },
    component: Main,
    children: [
      {
        path: 'create_user_page',
        name: 'create_user',
        meta: {
          icon: 'md-trending-up',
          title: '激活码生成'
        },
        component: () => import('@/view/new-accounts/new-accounts.vue')
      },
      {
        path: 'modify_user_page',
        name: 'modify_user',
        meta: {
          icon: 'md-pause',
          title: '修改账户权限'
        },
        component: () => import('@/view/components/tables/tables.vue')
      },
      {
        path: 'modify_password_page',
        name: 'modify_password',
        meta: {
          icon: 'logo-markdown',
          title: '修改账户密码'
        },
        component: () => import('@/view/components/editor/editor.vue')
      }
    ]
  },
  {
    path: '/books',
    name: 'books',
    meta: {
      icon: 'md-cloud-upload',
      title: '图书管理'
    },
    component: Main,
    children: [
      {
        path: 'list',
        name: 'booklist',
        meta: {
          icon: 'ios-document',
          title: '图书管理'
        },
        component: () => import('@/view/import-book/uploadFile.vue')
      },
      {
        path: 'import_guidance',
        name: 'import_guidance',
        meta: {
          icon: 'md-clipboard',
          title: '亲子阅读指导导入'
        },
        component: () => import('@/view/bookshelf-page/bookshelf-page.vue')
      },
      {
        path: 'import_ebook',
        name: 'import_ebook',
        meta: {
          icon: 'md-clipboard',
          title: 'E_book 导入'
        },
        component: () => import('@/view/E-book/E-book.vue')
      },
      {
        path: 'import_assignment',
        name: 'import_assignment',
        meta: {
          icon: 'md-clipboard',
          title: '阅读拓展导入'
        },
        component: () => import('@/view/assignment-page/assignment-page.vue')
      },
      {
        path: 'import_game',
        name: 'import_game',
        meta: {
          icon: 'md-clipboard',
          title: '游戏素材导入'
        },
        component: () => import('@/view/update/update-paste.vue')
      }
    ]
  },
  {
    path: 'student_statistics',
    name: 'student_statistics',
    meta: {
      icon: 'md-clipboard',
      title: '学生数据统计'
    },
    component: Main,
    children: [
      {
        path: 'progress',
        name: 'progress',
        meta: {
          icon: 'md-add',
          title: '学习进度统计'
        },
        component: () => import('@/view/excel/upload-excel.vue')
      }
    ]
  },
  {
    path: 'manage_message',
    name: 'manage_message',
    meta: {
      icon: 'md-clipboard',
      title: '社群消息管理'
    },
    component: Main,
    children: [
      {
        path: 'send_new_message',
        name: 'send_new_message',
        meta: {
          icon: 'md-add',
          title: '发布新消息'
        },
        component: () => import('@/view/excel/upload-excel.vue')
      },
      {
        path: 'check_message',
        name: 'check_message',
        meta: {
          icon: 'md-download',
          title: '审核历史消息'
        },
        component: () => import('@/view/excel/export-excel.vue')
      }
    ]
  },
  {
    path: '/401',
    name: 'error_401',
    meta: {
      hideInMenu: true
    },
    component: () => import('@/view/error-page/401.vue')
  },
  {
    path: '/500',
    name: 'error_500',
    meta: {
      hideInMenu: true
    },
    component: () => import('@/view/error-page/500.vue')
  },
  {
    path: '*',
    name: 'error_404',
    meta: {
      hideInMenu: true
    },
    component: () => import('@/view/error-page/404.vue')
  },
  {
    path: '/reviewInfo',
    name: 'review-info',
    component: Main,
    meta: {
      hideInMenu: true
    }
  },
  {
    path: '/generate_accounts',
    name: 'generate_accounts',
    component: Main,
    meta: {
      hideInMenu: true
    },
    children: [
      {
        path: 'fill_generate_info',
        name: 'fill_generate_info',
        meta: {
          title: '完善信息',
        },
        component: () => import('@/view/new-accounts/new-accounts.vue')
      },
      {
        path: 'generate_accounts',
        name: 'generate',
        meta: {
          title: '确认生成'
        },
        component: () => import('@/view/new-accounts/generate-accounts.vue')
      },
      {
        path: 'generate_result',
        name: 'generate_result',
        meta: {
          title: '生成结果'
        },
        component: () => import('@/view/new-accounts/generate-result.vue')
      }
    ]
  },
  {
    path: '/book',
    name: 'book',
    component: Main,
    meta: {
      hideInMenu: true
    },
    children: [
      {
        path: ':id',
        name: 'book-info',
        meta: {
          title: "本书详情"
        },
        component: () => import('@/view/book-detail-page/book-detail.vue')
      }
    ]
  },
  {
    path: '/import_assignment',
    name: 'import_assignment',
    component: Main,
    meta: {
      hideInMenu: true
    },
    children: [
      {
        path: 'assignment_success',
        name: 'assignment_success',
        meta: {
          title: '阅读拓展导入',
        },
        component: () => import('@/view/assignment-page/assignment-success.vue')
      }
    ]
  }
]

