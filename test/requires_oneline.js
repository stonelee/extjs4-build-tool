Ext.define('CIIS.view.Viewport', {
	extend : 'Ext.container.Viewport',
	layout : 'fit',
	requires : [ 'CIIS.view.HeaderPanel', 'CIIS.view.SidebarPanel', 'CIIS.view.MainPanel', 'CIIS.view.FooterPanel' ],

	initComponent : function() {
		// 设置布局
		this.items = {
			layout : 'border',
			border : 0,
			items : [ {
				xtype : 'headerpanel',
				region : 'north'
			}, {
				xtype : 'sidebar',
				region : 'west'
			}, {
				xtype : 'main',
				region : 'center'
			}, {
				xtype : 'footer',
				region : 'south'
			} ]
		};
		
		this.callParent();
	}
});
