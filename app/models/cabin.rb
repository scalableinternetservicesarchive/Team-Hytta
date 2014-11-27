class Cabin < ActiveRecord::Base
	belongs_to :user
	has_many :posts, dependent: :destroy
	validates :user, presence: true
end
