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
    path: '',
    name: 'doc',
    meta: {
      title: '弗恩英语官网',
      href: 'https://hf.vronedu.com/',
      icon: 'ios-book'
    }
  },
  {
    path: '/manage_user_page',
    name: 'manageUser',
    meta: {
      icon: 'logo-buffer',
      title: '用户权限管理'
    },
    component: Main,
    children: [
      {
        path: 'create_user_page',
        name: 'createUser',
        meta: {
          icon: 'md-trending-up',
          title: '新建账户'
        },
        component: () => import('@/view/new-accounts/new-accounts.vue')
      },
      {
        path: 'modify_user_page',
        name: 'modifyUser',
        meta: {
          icon: 'md-pause',
          title: '修改账户权限'
        },
        component: () => import('@/view/components/tables/tables.vue')
      },
      {
        path: 'modify_password_page',
        name: 'modifyPassword',
        meta: {
          icon: 'logo-markdown',
          title: '修改账户密码'
        },
        component: () => import('@/view/components/markdown/markdown.vue')
      }
    ]
  },
  {
    path: '/book_manage',
    name: 'book_manage',
    meta: {
      icon: 'md-cloud-upload',
      title: '数据上传'
    },
    component: Main,
    children: [
      {
        path: 'import_books',
        name: 'import_books',
        meta: {
          icon: 'ios-document',
          title: '创建新书'
        },
        component: () => import('@/view/importBook/uploadFile.vue')
      },
      {
        path: 'parent_child_instruct',
        name: 'parent_child_instruct',
        meta: {
          icon: 'md-clipboard',
          title: '亲子阅读指导导入'
        },
        component: () => import('@/view/update/update-paste.vue')
      },
      {
        path: 'ebook-import',
        name: 'ebook_import',
        meta: {
          icon: 'md-clipboard',
          title: 'E_book 导入'
        },
        component: () => import('@/view/update/update-paste.vue')
      },
      {
        path: 'exercise_import',
        name: 'exercise_import',
        meta: {
          icon: 'md-clipboard',
          title: '阅读拓展导入'
        },
        component: () => import('@/view/assignment/assignment.vue')
      },
      {
        path: 'game_import',
        name: 'game_import',
        meta: {
          icon: 'md-clipboard',
          title: '游戏素材导入'
        },
        component: () => import('@/view/update/update-paste.vue')
      }
    ]
  },
  {
    path: 'data_static',
    name: 'data_static',
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
    path: 'message_manage',
    name: 'message_manage',
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
    name: 'generateAccounts',
    component: Main,
    meta: {
      hideInMenu: true
    },
    children: [
      {
        path: 'fill_generate_info',
        name: 'fill_info',
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
