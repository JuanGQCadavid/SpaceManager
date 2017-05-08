DELIMITER //

CREATE FUNCTION POTENCIA_CINCO (numeroInicial INT)
returns INT

BEGIN
	SET @TIMES = 1;
    SET @RESULT = numeroInicial;
    
	labelname: REPEAT
    
		SET @RESULT = @RESULT * numeroInicial;
        SET @TIMES = @TIMES + 1;
	UNTIL @TIMES = 5
    
    END REPEAT labelname;
        
	RETURN @RESULT;


END//

DELIMITER ;