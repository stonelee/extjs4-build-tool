Ext.define('CIIS.view.constant.List', {
	extend : 'Ext.panel.Panel',
	alias : 'widget.constant_list',
	requires : [ 'CIIS.view.constant.administrativeduty.List'
	 , 'CIIS.view.constant.administrativerank.List',
	 'CIIS.view.constant.incumbencystatus.List',
	 'CIIS.view.constant.mothballcadre.List',
	 'CIIS.view.constant.personnelpoststype.List',
	 'CIIS.view.constant.politicsstatus.List',
	 'CIIS.view.constant.professional.List',
	 'CIIS.view.constant.professionaltechnicalpostrank.List'
	],
	layout : 'fit',
	border : 0,
	initComponent: function() {
		this.items = {
			xtype: 'tabpanel',
			activeTab: 0,
			plain: true,
			defaults: {
				bodyPadding: 10
			},
			items:[{
				 xtype: 'administrative_dutie_list'
				 },
				 {
				 xtype: 'administrative_rank_list'
				 },
				 {
				 xtype: 'incumbency_status_list'
				 },
				 {
				 xtype: 'mothball_cadre_list'
				 }, 
				 {
				 xtype: 'peoplenel_posts_type_list'
				 },	 
				 {
				 xtype: 'politics_status_list'
				 },
				 {
				 xtype: 'professional_list'
				 }, 
				 {
				 xtype: 'professional_technical_post_rank_list'
				 }]
		};
		this.callParent();
	},
});

