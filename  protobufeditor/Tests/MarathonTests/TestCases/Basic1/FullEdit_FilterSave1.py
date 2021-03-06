useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_03'

	if window('Protocol Buffer Editor'):
		click('Choose File')

		if window('Open'):
			select(commonBits.selectPane(), 'ams_locdownload_20041228.bin')
			click('Open')
		close()

		click('Edit1')
		click('Filter1')
		select('Table1', 'Loc_Type', 'Field,0')
		select('Table1', 'st', 'Value,0')
		select('Table1', 'cell:Field,2(null)')
		click('Save1')
		##select('FileChooser', commonBits.userDir() + 'Filter' + commonBits.fileSep() + 'xx1')
		commonBits.selectFileName(select, commonBits.userDir() + 'Filter' + commonBits.fileSep() + 'xx1')
		click('Save1')
		select_menu('Window>>ams_locdownload_20041228.bin>>Filter Options')
		click('Filter1')
		select('Table', 'cell:4|Loc_Name,0(Bankstown)')
		assert_p('Table', 'Text', 'Bankstown', '4|Loc_Name,0')
		select('Table', 'cell:3|Loc_Type,1(ST)')
		rightclick('Table', '3|Loc_Type,1')
		select_menu('Edit Record')
##		select('Table1', 'cell:3|Loc_Type,1(ST)')
		select('Table', 'cell:Data,5(58 Leland Street)')
		assert_p('Table', 'Text', 'Penrith', 'Data,6')
		select('Table', 'cell:Data,5(58 Leland Street)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5019, 5019], [Loc_Type, 3, , ST, ST], [Loc_Name, 4, , Penrith, Penrith], [Loc_Addr_Ln1, 5, , Penrith, Penrith], [Loc_Addr_Ln2, 6, , 58 Leland Street, 58 Leland Street], [Loc_Addr_Ln3, 7, , Penrith, Penrith], [Loc_Postcode, 8, , 2750, 2750], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
		select('Table', 'cell:Data,5(58 Leland Street)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:3|Loc_Type,1(ST)')
		select('Table', 'cell:3|Loc_Type,1(ST)')
		select_menu('Window>>ams_locdownload_20041228.bin>>Table:')
		select('Table2', 'cell:3|Loc_Type,1(ST)')
		select_menu('View>>Execute Saved Filter')
		#select('FileChooser', commonBits.userDir() + 'Filter'  + commonBits.fileSep() +'xx1')
		commonBits.selectFileName(select, commonBits.userDir() + 'Filter' + commonBits.fileSep() + 'xx1')

		click('Run')
		select('Table', 'cell:4|Loc_Name,2(Blacktown)')
		assert_p('Table', 'Text', 'Blacktown', '4|Loc_Name,2')
		select('Table', 'cell:4|Loc_Name,5(Eastwood)')
		rightclick('Table', '4|Loc_Name,5')
		select_menu('Edit Record')
##		select('Table1', 'cell:4|Loc_Name,5(Eastwood)')
		select('Table', 'cell:Data,4(Marayong Offsite Reserve)')
		assert_p('Table', 'Text', 'Marayong Offsite Reserve', 'Data,4')
		select('Table', 'cell:Data,4(Marayong Offsite Reserve)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5052, 5052], [Loc_Type, 3, , ST, ST], [Loc_Name, 4, , Eastwood, Eastwood], [Loc_Addr_Ln1, 5, , Marayong Offsite Reserve, Marayong Offsite Reserve], [Loc_Addr_Ln2, 6, , 11 Melissa Place, 11 Melissa Place], [Loc_Addr_Ln3, 7, , Marayong, Marayong], [Loc_Postcode, 8, , 2148, 2148], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
	close()
