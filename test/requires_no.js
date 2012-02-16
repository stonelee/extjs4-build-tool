Ext.define('CIIS.view.archive.List', {
	extend: 'Ext.panel.Panel',
	alias: 'widget.archive_list',
	layout: 'fit',
	border: 0,
	bodyPadding: 5,

	initComponent: function() {
		this.items = {
			xtype: 'tabpanel',
			plain: true,
			defaults: {
				bodyPadding: 5
			}
		};
		this.callParent();
	}

});

