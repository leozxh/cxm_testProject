#id仓库，放置所有页面元素id

from common.common_fun import Common,By

#登录操作
class Login(Common):
    #登录界面元素
    #账号输入框
    username_type=(By.ID,'com.zhiyi.cxm.caixm_prep:id/et_login_username')
    #密码输入框
    password_type=(By.ID,'com.zhiyi.cxm.caixm_prep:id/login_password')
    #登录按钮
    loginBtn=(By.ID,'com.zhiyi.cxm.caixm_prep:id/login_btn')

    #退出操作相关元素
    #左侧相同tab
    personalCenter = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tab_textview')
    #退出登录
    logoutBtn=(By.ID,'com.zhiyi.cxm.caixm_prep:id/btn_login_out')
    #确定按钮
    confirmBtn=(By.ID,'com.zhiyi.cxm.caixm_prep:id/confirm_button')

#收银主页
class Cashierhomepage(Common):
    # 收银主页选择批次
    tvTitle = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_title')
    # 收银主页货品列表选择货品
    saleNametv = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/sale_name_tv')
    # 数量、重量输入框
    layoutextfeeContainer = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/layout_ext_fee_container')
    # 数字键盘
    btnNumber = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_number')
    # 数字键盘确定按钮
    tvCommit = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_commit')
    # 确定按钮
    confirmButton = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/confirm_button')
    # 下单按钮
    cashierchoosedopenOrder = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/cashier_choosed_open_order')
    # 收银按钮
    btncheckOut = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_checkout')
    # 开码单
    btnsavesingleCode = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_save_single_code')
    # 查看买家列表
    showUser = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/iv_show_select_user')
    # 整单赊欠
    tvfinanceCredit = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_finance_credit')
    # 上一单票号
    tvrightMsg = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_right_msg')
    # 码单中心
    tvrightButton = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_right_button')
    # 码单中心返回键
    tvactionbarBack = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_action_bar_back')
    # 新增买家按钮
    btnaddCustomer = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_add_customer')
    # 买家姓名输入框
    customerName = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/customer_dialog_name_et')
    # 买家手机号输入框
    customerPhone = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/customer_dialog_phone_et')
    # 买家车牌号
    carNo = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/customer_dialog_car_no_et')
    # 新增买家保存按钮
    customersureBtn = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/customer_dialog_sure_btn')
    # 地磅开关
    truckweightswitchLayout = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/truck_weight_switch_layout')
    # 添加多客户
    layoutaddOrder = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/layout_add_order')
    # 添加备注
    layoutRremark = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/layout_remark')
    # 备注\三轮车费输入框
    inputValue = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/et_input_value')
    # 确定新增备注\三轮车费按钮
    tvSure = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_sure')
    # 添加三轮车费
    layoutadditionalFee = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/layout_additional_fee')
    # 购物车删除临时客户
    ivDelete = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/iv_delete')
    #购物车显示的新增买家
    tvcustomerName = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_customer_name')

#码单中心
class Codelistcenter(Common):
    #码单中心按钮
    tvrightButton = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_right_button')

#主流程
class Mainprocess(Common):
    # 货品库存界面元素
    # 货品库存的按钮（左侧tab栏的，相同的resource_id)
    sameBtn = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tab_textview')
    # 库存管理tab、货品管理tab、货主管理tab（顶部tab栏的，相同的resource_id)
    goodsManagement = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_tab_title')
    # 新增货品按钮
    addNewgoods = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/add_layout')
    # 货品名称输入框、规格输入框、销售单价输入框、货主姓名输入框
    setgoodsName = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/et_view')
    # 保存按钮
    saveBtn = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_save')
    # 新增批次按钮
    addNewbatch = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_bantch')
    # 新增货主
    addShipper = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_add_shipper')
    # 选择货主
    chooseShipper = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/item_layout')
    # 下一步
    nextStep = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_next_step')
    # 选择货品
    chooseProduct = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_goods_name')
    # 数字键盘
    btnNumber = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_number')
    # 数字键盘确定按钮
    tvCommit = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_commit')
    # 确定入库
    tvConfirm = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_confirm')
    # 收银主页选择批次
    tvTitle = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_title')
    # 收银主页货品列表选择货品
    saleNametv = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/sale_name_tv')
    # 数量、重量输入框
    layoutextfeeContainer = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/layout_ext_fee_container')
    # #确定按钮
    # confirmButton = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/confirm_button')
    # 下单按钮
    cashierchoosedopenOrder = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/cashier_choosed_open_order')
    # 收银按钮
    btncheckOut = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_checkout')
    # 开码单
    btnsavesingleCode = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_save_single_code')

#还款
class Repayment(Common):
    # 货品库存的按钮（左侧tab栏的，相同的resource_id)
    sameBtn = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tab_textview')
    # 收银主页选择批次
    tvTitle = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_title')
    # 收银主页货品列表选择货品
    saleNametv = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/sale_name_tv')
    # 数量、重量输入框
    layoutextfeeContainer = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/layout_ext_fee_container')
    # 数字键盘
    btnNumber = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_number')
    # 数字键盘确定按钮
    tvCommit = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_commit')
    # 下单按钮
    cashierchoosedopenOrder = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/cashier_choosed_open_order')
    # 收银按钮
    btncheckOut = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_checkout')
    # 查看买家列表
    showUser = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/iv_show_select_user')
    # 整单赊欠
    tvfinanceCredit = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_finance_credit')
    # 买家管理、订单管理tab
    tvtabTitle = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_tab_title')
    # 查看订单
    tvView = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_view')
    # 还款按钮
    btnbillRepay = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_bill_repay')
    # 还款收银按钮
    btnrepayOrder = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_repay_order')





