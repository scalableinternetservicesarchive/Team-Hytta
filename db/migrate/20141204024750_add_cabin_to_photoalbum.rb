class AddCabinToPhotoalbum < ActiveRecord::Migration
  def change
  	  	add_column :photoalbums, :cabin_id, :integer
    	add_column :photoalbums, :user_id, :integer
  end
end
