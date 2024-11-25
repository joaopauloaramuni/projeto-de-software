public class UserDAOImpl implements UserDAO {
    @Override
    public void save(User user) {
        // Código para salvar o usuário no banco de dados
        System.out.println("User saved: " + user.getName());
    }

    @Override
    public User findById(int id) {
        // Código para buscar o usuário no banco de dados
        return new User(); // Retorna um novo usuário como exemplo
    }

    @Override
    public void update(User user) {
        // Código para atualizar o usuário no banco de dados
        System.out.println("User updated: " + user.getName());
    }

    @Override
    public void delete(int id) {
        // Código para deletar o usuário do banco de dados
        System.out.println("User deleted with id: " + id);
    }
}
