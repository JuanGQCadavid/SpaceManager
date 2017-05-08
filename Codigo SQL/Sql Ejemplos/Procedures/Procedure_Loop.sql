
delimiter //

CREATE PROCEDURE noseDeja (INOUT numero INT)

BEGIN
	
    lablename: LOOP
		SET numero = numero + 1;
        
        IF numero < 10 THEN 
			ITERATE lablename;
            
		ELSEIF numero > 10 THEN
			SET Jupiter = 10;
            
		ELSE 
			SET Jupiter = 15;
            
		END IF;
        
        LEAVE lablename;
	END LOOP lablename;

END//

delimiter ;