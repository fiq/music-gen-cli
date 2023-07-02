{
  description = "Music Gen CLI Flake with a good example of python ml dependencies";
  inputs.nixpkgs.url = "github:nixos/nixpkgs/23.05";
 
  outputs = { self, nixpkgs }:
    let 
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system}.pkgs;
      lib = nixpkgs.lib;
    in {
      nixpkgs.config.cudaSupport = true;
      nixpkgs.config.allowUnfree= true;
      

      devShells.${system}.default = pkgs.mkShell {
        name = "Music Gen Cli Environment";
        buildInputs = import ./nix-pkgs.nix pkgs;
        shellHook = "
          source ./nix-shell-entry.sh
        ";
    };
  };
}
