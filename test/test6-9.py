import easygui
burger = easygui.choicebox("今天早餐想吃什麼呢?" , choices= ["滿福堡","豬肉滿福堡","豬肉滿福堡加蛋","滿福香雞堡","滿福鮮蔬堡"])
drinks = easygui.choicebox("請選附餐飲料:" , choices= ["可口可樂","雪碧","紅茶"])
cup = easygui.choicebox(drinks , choices= ["大杯","中杯","小杯"])
easygui.msgbox("你點了" + burger + ",附餐飲料是" + cup + drinks)