Library ieee; 
use ieee.std_logic_1164.all; 

entity not_vhdl is
   port(a:in  std_logic;
	     q:out std_logic
   ); 
end not_vhdl; 
 
architecture main of not_vhdl is
begin
   q <= not q;
end main; 
