class Todolist < ActiveRecord::Base
	belongs_to :cabin
	belongs_to :user
	validates :cabin, presence: true
end
