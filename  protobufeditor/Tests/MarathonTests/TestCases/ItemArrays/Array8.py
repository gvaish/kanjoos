useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() +  'protoStoreSales7.bin')
		click('Edit1')
		##select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'Product')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63604808, [40118], [1], [4870], [SALE], [4.87], [4.87], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 69684558, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , 69694158, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 62684671, [40118, 40118], [1, -1], [69990, -69990], [SALE, RETURN], [69.99, -69.99], [69.99, -69.99], [\'\',\' -1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 65674532, [40118], [1], [3590], [SALE], [3.59], [3.59], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63674861, [40118], [10], [2700], [SALE], [2.7], [2.7], [\'\']], [, , 64634429, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , 66624458, [40118], [1], [890], [SALE], [0.89], [0.89], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ]]')
		##select('JTreeTable', '')
		select('JTreeTable', 'cell:priceFloat,8([19.0, -19.0, 5.01])')
		select('TextField', '[19.0, -19.0123, 456.012, 5.01]')
		keystroke('TextField', 'Tab')
		select('JTreeTable', 'cell:priceDouble,9([19.0, -19.0, 5.01])')
		assert_p('JTreeTable', 'Text', 'cell:priceDouble,9([19.0, -19.0, 5.01])')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63604808, [40118], [1], [4870], [SALE], [4.87], [4.87], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 69684558, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0123, 456.012, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , 69694158, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 62684671, [40118, 40118], [1, -1], [69990, -69990], [SALE, RETURN], [69.99, -69.99], [69.99, -69.99], [\'\',\' -1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 65674532, [40118], [1], [3590], [SALE], [3.59], [3.59], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63674861, [40118], [10], [2700], [SALE], [2.7], [2.7], [\'\']], [, , 64634429, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , 66624458, [40118], [1], [890], [SALE], [0.89], [0.89], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ]]')
		select('JTreeTable', 'cell:priceFloat,8([19.0, -19.0123, 456.012, 5.01])')
		##select('JTreeTable', '')
		select('JTreeTable', 'cell:priceFloat,8([19.0, -19.0123, 456.012, 5.01])')
		click('ArrowButton')
		assert_p('Table', 'Content', '[[0, 19.0], [1, -19.0123], [2, 456.012], [3, 5.01]]')
		select('Table', 'cell:Data,3(5.01)')
		select('Table', '5.0123', 'Data,3')
		select('Table', 'cell:Data,2(456.012)')
		assert_p('Table', 'Content', '[[0, 19.0], [1, -19.0123], [2, 456.012], [3, 5.0123]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		assert_p('JTreeTable', 'Text', '')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63604808, [40118], [1], [4870], [SALE], [4.87], [4.87], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 69684558, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0123, 456.012, 5.0123], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , 69694158, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 62684671, [40118, 40118], [1, -1], [69990, -69990], [SALE, RETURN], [69.99, -69.99], [69.99, -69.99], [\'\',\' -1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 65674532, [40118], [1], [3590], [SALE], [3.59], [3.59], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63674861, [40118], [10], [2700], [SALE], [2.7], [2.7], [\'\']], [, , 64634429, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , 66624458, [40118], [1], [890], [SALE], [0.89], [0.89], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ]]')

	close()