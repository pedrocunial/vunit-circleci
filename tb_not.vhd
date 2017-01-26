library ieee;
use ieee.std_logic_1164.all;

library vunit_lib;
context vunit_lib.vunit_context;

entity tb_not is
  generic (runner_cfg : string);
end entity;

architecture tb of tb_not is

  component not_vhdl is
		port(a:in  std_logic;
			  q:out std_logic
		); 
   end component;

   signal  inA, outQ : std_logic;

begin

  mapping: not_vhdl port map(inA, outQ);

  main : process
  begin
    test_runner_setup(runner, runner_cfg);

      -- Teste: 0 
      inA <= '0';
      wait for 200 ps;
      assert(outQ = '1')  report "Falha em teste: not 0 != 1" severity error;

      -- Teste: 1
      inA <= '1';
      wait for 200 ps;
      assert(outQ = '0')  report "Falha em teste: not 1 != 0" severity error;

    test_runner_cleanup(runner); -- Simulation ends here

  end process;
end architecture;
