
delimiter //

CREATE PROCEDURE SiSenor (INOUT numero INT)

BEGIN
	DECLARE Jupiter INT default 10;
    
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