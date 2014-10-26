class CreateCabins < ActiveRecord::Migration
  def change
    create_table :cabins do |t|
      t.string :navn
      t.string :address
      t.text :descritpion

      t.timestamps
    end
  end
end
