class AddCabinToTodolist < ActiveRecord::Migration
  def change
  	  	add_column :todolists, :cabin_id, :integer
    	add_column :todolists, :user_id, :integer
  end
end
