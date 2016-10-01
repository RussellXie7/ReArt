(function(){
	jQuery(document).ready(function(){
		
		// Nav Menu (current class)
		var $menuItems = $(".header nav li a"),
			lastId,
			fromTop,
			cur,
			scrollItems = $menuItems.map(function() {
				var item = $($(this).attr("href"));
				if (item.length) return item; 
			});
			
		// click nav
		$menuItems.on('click', function(e) {
			var href  = $(this).attr("href"),
			offsetTop = $(href).offset().top + 10 + 'px';
			$('html, body').stop().animate({scrollTop: offsetTop}, 1000, 'easeOutCubic');
			e.preventDefault();
		});
		
		// add current class to menu
        $(window).scroll(function(){
			fromTop = $(this).scrollTop() + 10,
			cur = scrollItems.map( function() {
				if ($(this).offset().top < fromTop) return this;
			});
			cur = cur[cur.length-1];
			var id = cur && cur.length ? cur[0].id : "";
			if (lastId !== id) {
				lastId = id;
				$menuItems.parent().removeClass("current").end().filter("[href=#"+id+"]").parent().addClass("current");
			} 
		});
		
	});
})();