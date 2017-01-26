Library ieee; 
use ieee.std_logic_1164.all; 

entity nand_vhdl is
   port(a:in  std_logic;
	     b:in  std_logic;
	     q:out std_logic
   ); 
end nand_vhdl; 
 
architecture main of nand_vhdl is
signal tmp1, tmp2 : std_logic;
begin
   tmp1 <= a nand b;
   tmp2 <= not tmp1;
	q    <= not tmp2;
end main; 
