Library ieee; 
use ieee.std_logic_1164.all; 

entity nor_vhdl is
   port(a:in  std_logic;
	     b:in  std_logic;
	     q:out std_logic
   ); 
end nor_vhdl; 
 
architecture main of nor_vhdl is
begin
   q <= a nor b;
end main; 
