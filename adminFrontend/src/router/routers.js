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
          title: '生成激活码'
        },
        component: () => import('@/view/new-accounts')
      }
    ]
  },
  {
    path: '/book',
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
          title: '图书列表'
        },
        component: () => import('@/view/booklist')
      },
      {
        path: ':id',
        name: 'book',
        meta: {
          hideInMenu: true,
          title: '图书信息'
        },
        component: () =>
          import ('@/view/book-info')
      },
      {
        path: ':id/ebook',
        name: 'ebook',
        meta: {
          hideInMenu: true,
          title: '图书信息'
        },
        component: () => import('@/view/E-book')
      },
      {
        path: ':id/guidance',
        name: 'guidance',
        meta: {
          hideInMenu: true,
        },
        component: () => import('@/view/guidance')
      },
      {
        path: ':id/assignment',
        name: 'assignment',
        meta: {
          hideInMenu: true
        },
        component: () => import('@/view/assignment')
      },
      {
        path: ':id/game',
        name: 'game',
        meta: {
          hideInMenu: true
        },
        component: () => import('@/view/import-game')
      }
    ]
  },
  {
    path: '/student',
    name: 'students',
    meta: {
      icon: 'md-contacts',
      title: '学生管理',
    },
    component: Main,
    children: [
      {
        path: 'userlist',
        name: 'userlist',
        meta: {
          icon: 'md-contacts',
          title: '学生列表'
        },
        component: () => import('@/view/user-list/index.vue')
      },
      {
        path: ':id',
        name: 'user-detail',
        meta: {
          hideInMenu: true,
          title: '学生详细信息'
        },
        component: () => import('@/view/user-list/detail.vue')
      }
    ]
  },
  {
    path: '/notice',
    name: 'notices',
    meta: {
      icon: 'md-contacts',
      title: '消息管理',
    },
    component: Main,
    children: [
      {
        path: 'noticelist',
        name: 'noticelist',
        meta: {
          icon: 'md-contacts',
          title: '消息列表'
        },
        component: () => import('@/view/notice/index.vue')
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
  }
]

