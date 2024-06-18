export enum Roles {
  Administrador = 'administrador',
  Cliente = 'cliente',
  Trabajador = 'trabajador',
}

export const RolesRoutes = {
  [Roles.Administrador]: 'admin',
  [Roles.Cliente]: 'client',
  [Roles.Trabajador]: 'worker',
}

export const RolesNumbers = {
  [Roles.Administrador]: 3,
  [Roles.Cliente]: 1,
  [Roles.Trabajador]: 2,
}


export const rolesArray = Object.values(Roles);
